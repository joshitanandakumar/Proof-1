import numpy as np

print("Player 1 will use X. Player 2 will use O.\nPlayer 1, enter the row and column position.")

board = np.array([['_', '_', '_'],
                  ['_', '_', '_'],
                  ['_', '_', '_']])
     n 
def checkwin():
    if (rowWinner()):
        return True
    elif (colWinner()):
        return True
    elif (leftDiagWinner()):
        return True
    else:
        return (rightDiagWinner())

def checkdraw():
    if '_' in board:
        return False
    else:
        print("The game ends in a draw. Try again next time!")
        return True

def positionTaken(pos):
    
    if board[pos[0]][pos[1]] == '_':
        return False
    else:
        print("Position already taken. Please choose another position.")
        return True

def gameBoard():    

    while True:
        player1pos = []
        print("Enter player 1 position:")
        player1pos = [int(x) - 1 for x in input().split(',')]
        while positionTaken(player1pos):
            player1pos = [int(x) - 1 for x in input().split(',')]
        board[player1pos[0]][player1pos[1]] = 'X'
        print(board)
        if (checkwin()):
            print("Player 1 wins")
            break
        if (checkdraw()):
            break
        player2pos = []
        print("Enter player 2 position:")
        player2pos = [int(x) -1 for x in input().split(',')]
        while positionTaken(player2pos):
            player2pos = [int(x) - 1 for x in input().split(',')]
        board[player2pos[0]][player2pos[1]] = 'O'
        print(board)
        if (checkwin()):
            print("Player 2 wins")
            break
        if (checkdraw()):
            break
    
 
    return board


def rowWinner():
    not_matched = False
    for i in range(0,3):
        not_matched = False
        value = board[i][0]
        if value == '_':
            continue
        for j in range(1,3):
            if board[i][j] != value:
                not_matched = True
                break
        if (not_matched == False):
            return True
    return False

def colWinner():
    not_matched = False
    for j in range(0,3):
        not_matched = False
        value = board[0][j]
        if value == '_':
            continue
        for i in range(1,3):
            if board[i][j] != value:           
                not_matched = True
                break
        if (not_matched == False):
            return True
    return False

def leftDiagWinner():
    value = board[0][0]
    not_matched = False
    for i in range(1,3):
        if value == '_':
            not_matched = True
            break
        if board[i][i] != value:
            not_matched = True
            break
    if (not_matched == False):
        return True
    return False
    
def rightDiagWinner():
    value = board[0][2]
    if value == '_':
        return False
    elif board[1][1] and board [2][0] == value:
        return True
    else:
        return False




gameBoard()



