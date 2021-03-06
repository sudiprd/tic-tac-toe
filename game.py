# display
# display board
# play game
# handle turn
# check winner
#     check by row
#     check by column
#     check by diagonal
# flip player

#----------- Global variable-------

#----- game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"] 

# if game is still going
game_still_going = True

# who won ? who tie ?
winner= None

# whos turn is it
current_player ="X"
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# play a game of tic-tac-toe
def play_game():
    # display initial board
    display_board()

    while game_still_going:
    
    # handle a single turn of a arbitrary player
        handle_turn(current_player)
    #  check if the game has ended
        check_if_game_over()
    #  flip to other player
        flip_player()    

if winner == "X" or winner =="O":
    print(winner + "won.")
elif  winner == None:
    print ("Tie.")

# handle a single turn of a arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9:")

    valid = False
    while not valid:
     while position not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:
      position = input("Invalid Input. Choose a position from 1-9:")

    position = int(position) -1

    if board[position] == "-":
        valid= True
    else :
        print("You cant go there. Go again.")


    board[position] = player
    display_board()


def check_if_game_over():
    
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # set a global varible
    global winner   
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_winner()
    # check diagonal
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner= column_winner
    elif diagonal_winner:
        winner = diagonal_winner    

    winner = None
    return 
def check_rows():
    #set up global variable
    global game_still_going
    # check if any of the rows have all the same value and is not empty
    row_1 = board[0] == board[1] == board [2] != "-"
    row_2 = board[3] == board[4] == board [5] != "-"
    row_3 = board[6] == board[7] == board [8] != "-"
    #if any row does have a match,flag that there is a win
    if row_1 or row_2 or row_3:
        # for ending the game need to be false
        game_still_going = False  

    # Return the winner X or 0  
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return

def check_column():
     #set up global variable
    global game_still_going
    # check if any of the rows have all the same value and is not empty
    column_1 = board[0] == board[3] == board [6] != "-"
    column_2 = board[1] == board[4] == board [7] != "-"
    column_3 = board[2] == board[5] == board [8] != "-"
    #if any row does have a match,flag that there is a win
    if column_1 or column_2 or column_3:
        # for ending the game need to be false
        game_still_going = False  
    # Return the winner X or 0  
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    
    return

def check_diagonal():
     #set up global variable
    global game_still_going
    # check if any of the rows have all the same value and is not empty
    diagonal_1 = board[0] == board[4] == board [8] != "-"
    diagonal_2 = board[2] == board[4] == board [6] != "-"

    #if any row does have a match,flag that there is a win
    if diagonal_1 or diagonal_2:
        # for ending the game need to be false
      game_still_going = False  
      

    # Return the winner X or 0  
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    
    return



def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player ==" X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"
    return
    play_game()
