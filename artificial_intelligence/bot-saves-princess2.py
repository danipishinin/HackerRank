#!/usr/bin/python

def nextMove(n,r,c,grid):
    princess = [0,0]
    # Finding Princess
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 'p'):
                princess = [i,j]

    # Moves to saves princess
    if(r < princess[0]):
        return 'DOWN'
    elif(r > princess[0]):
        return 'UP'
    elif(c < princess[1]):
        return 'RIGHT'
    elif(c > princess[1]):
        return 'LEFT'

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
