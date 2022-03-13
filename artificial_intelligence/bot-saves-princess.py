#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    princess = [0,0]
    bot = [0,0]
    # Finding Princess and Mario
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 'p'):
                princess = [i,j]
            if(grid[i][j] == 'm'):
                bot = [i,j]

    # Moves to saves princess
    while(bot[0] < princess[0]):
        bot[0] = bot[0] + 1
        print('DOWN')

    while(bot[0] > princess[0]):
        bot[0] = bot[0] - 1
        print('UP')
    
    while(bot[1] < princess[1]):
        bot[1] = bot[1] + 1
        print('RIGHT')

    while(bot[1] > princess[1]):
        bot[1] = bot[1] - 1
        print('LEFT')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
