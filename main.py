import random

# ----------Global Variable----------

Curr_player = "X"

Winner = None

game_still_going = True

# ------------------------------------

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


# display Board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    # Display the initial board
    display_board()

    while game_still_going:
        handle_turn(Curr_player)

        check_if_game_over()

        flip_player()

    if Winner == "X" or Winner == "O":
        print(Winner + " Won.")
    elif Winner is None:
        print("Tie.")


def check_if_game_over():
    check_for_winner()
    check_if_tie()
    return


def check_for_winner():
    global Winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()

    if row_winner:
        Winner = row_winner
    elif column_winner:
        Winner = column_winner
    elif diagonal_winner:
        Winner = diagonal_winner
    else:
        Winner = None
    return


def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

    # Return the winner
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_still_going = False

    # Return the winner
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_diagonal():
    global game_still_going

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_still_going = False

    # Return the winner
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[1]
    else:
        return None


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def handle_turn(player):
    if player == "X":
        print("Your Turn!!")
        position = input("Choose a position in between 1-9 ")

        valid = False
        while not valid:
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Choose a position in between 1-9 ")

            position = int(position) - 1
            if board[position] == "-":
                valid = True
            else:
                print("You can't go there. Go again.")

        board[position] = player

        display_board()
    else:

        position = random.randint(1, 9)

        valid = False
        while not valid:

            position = int(position) - 1
            if board[position] == "-":
                valid = True

        board[position] = player
        print("------------------------")
        display_board()


def flip_player():
    global Curr_player

    if Curr_player == "X":
        Curr_player = "O"
    elif Curr_player == "O":
        Curr_player = "X"
    return


# --------Execution of game-----------
play_game()
