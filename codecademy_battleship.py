###################################################
### Battleship text game.                       ###
### Exercise from Codecademy Python track.      ###
### http://www.codecademy.com/en/tracks/python  ###
###################################################

from random import randint

board = []

# allows player to set a board size
while True: 
    try:
        board_size = int(raw_input("Please enter a board size you prefer. The bigger the board, the more tries you will have. Anything under 20 is reasonable: "))
        break
    except:
        print "Please enter an positive number"

turns_allowed = board_size

for x in range(0, board_size):
    board.append(["O"] * board_size)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

# Generates the random location of the ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

turn = 0

for i in range(turns_allowed):
    
    print "Turn", turn + 1
    turn = turn + 1

    # asks user to guess the location of the ship
    while True: 
        try:
            guess_row = int(raw_input("Guess Row (0 to %s): " % (len(board) - 1)))
            break
        except:
            print "Please enter an positive number"

    while True:
        try:
            guess_col = int(raw_input("Guess Col (0 to %s): " % (len(board) - 1)))
            break
        except:
            print "Please enter an positive number"

    print ship_row
    print ship_col

    # checks the user guess after each turn
    if ship_row == guess_row and ship_col == guess_col:
        print "Congratulations! You sank the battleship!\n"
        break
    else:
        if guess_row not in range(board_size) or guess_col not in range(board_size):
            print "Oops, that's not even in the ocean.\n"
            if turn == turns_allowed:
                print "Game Over!"
        elif board[guess_row][guess_col] == "X":
            print "You tried that location before!.\n"
            if turn == turns_allowed:
                print "Game Over!"
        else: 
            print "You missed the battleship!\n"
            board[guess_row][guess_col] = "X"          
            print_board(board)
            if turn == turns_allowed:
                print "Game Over!\n" * board_size