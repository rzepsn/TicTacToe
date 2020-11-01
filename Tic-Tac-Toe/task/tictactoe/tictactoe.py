# global flags to keep game state
win_x = 0
win_o = 0
draw = 0
has_empty_fields = True
wrong_count = 0
end_game = False
error_occured = False
error_message = ""


# gets list of 9 strings as a board state


def print_board(board_state):
    if board_state == False:
        print("---------")
        print("| " + "      " + "|")
        print("| " + "      " + "|")
        print("| " + "      " + "|")
        print("---------")
    else:
        print("---------")
        print("| " + board_state[0] + " " + board_state[1] + " " + board_state[2] + " " + "|")
        print("| " + board_state[3] + " " + board_state[4] + " " + board_state[5] + " " + "|")
        print("| " + board_state[6] + " " + board_state[7] + " " + board_state[8] + " " + "|")
        print("---------")


# gets list of 9 strings as a board state, returns all straight lines to check


def get_straight_lines(board_state):
    straight_lines = []
    if len(board_state) == 9:
        straight_lines = [board_state[0:3], board_state[3:6], board_state[6:9], board_state[0:9:3], board_state[1:9:3],
                          board_state[2:9:3],
                          board_state[0:9:4], board_state[2:7:2]]
    return straight_lines


def check_for_empty_fields(board_list):
    global has_empty_fields
    if "_" in board_list:
        has_empty_fields = True
        # print("there are empty fields!")
    else:
        has_empty_fields = False
        # print("no empty fields left ;c  ")


def assess_the_board(board_list):
    global wrong_count, win_o, win_x, end_game, draw, error_occured, error_message

    straight_lines = get_straight_lines(board_list)
    check_for_empty_fields(board_list)

    if abs(board_list.count('X') - board_list.count('O')) >= 2:
        wrong_count = 1

    for i in straight_lines:
        if i == "XXX" and wrong_count == 0:
            win_x = 1
            end_game = True
        if i == "OOO" and wrong_count == 0:
            win_o = 1
            end_game = True
        if (win_o or win_x) and wrong_count:
            print("Impossible")

    if not has_empty_fields and not end_game:
        draw = 1
        end_game = True

    return end_game


def print_result():
    global draw, win_x, win_o
    if win_x:
        print("X wins")
    if win_o:
        print("O wins")
    if draw:
        print("Draw")


# takes input string with coordinates, returns list of integers
def get_coordinates_list(coordinates_str):
    global error_occured
    global error_message
    try:
        coordinates_list = [int(x) for x in coordinates_str.split()]
    except ValueError:
        error_occured = True
        error_message = "You should enter numbers!"
        print(error_message)
    return coordinates_list


def check_scope(coordinates_list):
    global error_occured
    global error_message
    if len(coordinates_list) != 2:
        error_occured = True
        error_message = "You should input exactly two numbers"

    for i in coordinates_list:
        if i not in range(1, 4):
            error_occured = True
            error_message = "Coordinates should be from 1 to 3!"
            print(error_message)

    return error_occured


# takes 2 coordinates, and returns one-digit list index
def get_simplified_index(coordinates_list):
    if not error_occured:
        x = coordinates_list[0] - 1
        y = abs(coordinates_list[1] - 3)
        converter = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        simplified_index = converter[y][x]
        return simplified_index


def check_if_empty(simple_index, board_list):
    if board_list == "_________":
        return True;

    global error_occured
    global error_message
    if not error_occured:
        if board_list[simple_index] != '_':
            error_occured = True
            error_message = "This cell is occupied! Choose another one!"
            print(error_message)
            if_empty = False
        else:
            if_empty = True

    return if_empty


def mark_a_move(simple_index, board_list, player):
    if not error_occured:
        board_list = board_list[:simple_index] + player + board_list[simple_index + 1:]
    return board_list


def switch_player(player):
    if player == "X":
        new_player = "O"
    if player == "O":
        new_player = "X"
    return new_player


print_board(False)
board_state = "_________"
player = "X"
while not end_game:
    coordinates_string = input("Enter the coordinates: ")
    coordinates_list = get_coordinates_list(coordinates_string)
    check_scope(coordinates_list)
    simple_index = get_simplified_index(coordinates_list)
    if_empty = check_if_empty(simple_index, board_state)
    if not error_occured:
        board_state = mark_a_move(simple_index, board_state, player)
        print_board(board_state)
        assess_the_board(board_state)
        player = switch_player(player)
    if end_game:
        print_result()
    if error_occured and not end_game:
        error_occured = False
        error_message = ""





