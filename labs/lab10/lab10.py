"""
Name: Michael Diorio
lab10.py
"""


def build_board():
    return list(range(1, 10))


def display_board(board):
    for i in range(3):
        j = i * 3
        print(str(board[j]) + "|" + str(board[j+1]) + "|" + str(board[j+2]))
        print("-----")


def fill_spot(board, pos, char):
    if char == "X" or char == "O":
        board[pos - 1] = char
    else:
        print("Not a valid spot.")


def is_legal(board, pos):
    return bool(1 <= pos <= 9 and pos == board[pos - 1])


def game_won(board, char):
    if board[0] and board[1] and board[2] == char:
        return True
    elif board[3] and board[4] and board[5] == char:
        return True
    elif board[6] and board[7] and board[8] == char:
        return True
    elif board[0] and board[3] and board[6] == char:
        return True
    elif board[1] and board[4] and board[7] == char:
        return True
    elif board[2] and board[5] and board[8] == char:
        return True
    elif board[0] and board[4] and board[8] == char:
        return True
    elif board[2] and board[4] and board[6] == char:
        return True

    return False


def game_over(board):
    if game_won(board, "X"):
        return True
    elif game_won(board, "O"):
        return True
    elif board[0:9] == "X" or "O":
        return True
    else:
        return False


def play_game():
    board = build_board()

    while True:
        display_board(board)
        pos = eval(input("Choose a spot by typing the corresponding number minus 1: "))

        while is_legal(board, pos - 1):
            fill_spot(board, pos-1, "X")
            if game_over(board):
                if game_won(board, "X"):
                    print("Player 1 wins :)")
                else:
                    print("It's a tie.")
                break
        while is_legal(board, pos):
            fill_spot(board, pos, "O")
            if game_over(board):
                if game_won(board, "O"):
                    print("Player 2 wins :)")
                else:
                    print("It's a tie.")
                break


def main():
    play_game()
    pass


main()
