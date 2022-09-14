#!/bin/python3

def nextMove(posr, posc, board):
    size_board = len(board)
    dirty_cells = [0,0]
    for i in range(size_board):
        for j in range(size_board):
            if(board[i][j] == 'd'):
                dirty_cells = [i,j]
                
    # Moves to clean cells
    if(posr < dirty_cells[0]):
        print('DOWN')

    elif(posr > dirty_cells[0]):
        print('UP')
    
    elif(posc < dirty_cells[1]):
        print('RIGHT')

    elif(posc > dirty_cells[1]):
        print('LEFT')
    else: 
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)