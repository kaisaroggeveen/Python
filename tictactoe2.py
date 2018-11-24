#OTHER INFO
fillboard = ['0','1','2','3','4','5','6','7','8']


#VOID FUNCTIONS
def locationBoard(board):
    print(board[0]+'|'+ board[1]+ '|'+ board[2])
    print(board[3]+'|'+ board[4]+ '|'+ board[5])
    print(board[6]+'|'+ board[7]+ '|'+ board[8])

def playerInput():
    marker = ""
    while marker != 'X' and marker != "O":
        marker =  input("Player 1: Choose X or O:").upper()
    if marker == "X":
        return ("X","O")
    else:
        return("O","X")
    
def playerMove():
    lastMove = 0
    if lastMove%2 == 0 and lastMove < 10:
        player1move = input("Player 1 where would you like to go?")
        fillboard[int(player1move)] = player1char
        player1moves = [] + [int(player1move)]
        allMoves = [] + [int(player1move)]
        print(locationBoard(fillboard))
    else:
        player2move = input("Player 2 where would you like to go?")
        while player2move == player1move:
            player2move = input("That spot has already been filled, enter a new location")
        fillboard[int(player2move)] = player2char
        player2moves = [] + [int(player2move)]
        allMoves = [] + [int(plaer2move)]
        print(locationBoard(fillboard))
    lastMove += 1
    
def winCheck(board, mark):
    return ((board[0] == board[4] == board[8] == mark) or
    (board[2] == board[4] == alist[6] == mark) or
    (board[0] == board[1] == board[2] == mark) or
    (board[3] == board[4] == board[5] == mark) or
    (board[6] == board[7] == board[8] == mark) or
    (board[0] == board[3] == board[6] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark))

#game play
player1char, player2char = playerInput()
playerMove()
