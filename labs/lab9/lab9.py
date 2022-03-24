"""
Scott Repik -Repiksh
lab9.py


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_list


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    string = str(board[position - 1])
    check = string.isnumeric()
    return check


def fill_spot(board, position, character):
    new_character = character.strip()
    board[position - 1] = new_character.lower()


def winning_game(board):
    for i in range(0, 8, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True


def game_over(board):
    if winning_game(board):
        return True
    for i in range(0,8):
        string_board = str(board[i])
        check = string_board.isnumeric()
        if check:
            return False



def get_winner(board):
    if game_over(board):
        count_x = board.count("x")
        count_o = board.count("o")
        if count_x > count_o:
            print("X wins")
        elif count_o == count_x:
            print("O wins")
        else:
            print("Its a tie")


def play(board):
    print_board(board)
    rerun = True
    while not game_over(board):
        pos = eval(input("What Spot To Place an X?"))
        check = is_legal(board, pos)
        if check:
            fill_spot(board, pos, "x")
        else:
            print("Can not place here")
        print_board(board)

        pos_o = eval(input("What Spot To Place an O?"))
        check_o = is_legal(board, pos_o)
        if check_o:
            fill_spot(board, pos_o, "o")
        else:
            print("Can not place here")
        print_board(board)

    get_winner(board)


def main():
    play(build_board())


if __name__ == '__main__':
    main()
