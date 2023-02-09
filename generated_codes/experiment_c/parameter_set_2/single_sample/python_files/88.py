'''


'''

import sys
sys.setrecursionlimit(10000)

def get_input():
    n, m, q = map(int, input().split())
    sx, sy = map(int, input().split())
    p = []
    for i in range(6):
        p.append(list(map(int, input().split())))
    t = []
    for i in range(q):
        t.append(int(input()))
    return n, m, q, sx, sy, p, t

def get_grid(n, m, sx, sy):
    grid = [[0]*m for i in range(n)]
    grid[sx-1][sy-1] = 1
    return grid

def get_cross(grid, i, j):
    cross = []
    for k in range(len(grid[i])):
        cross.append(grid[i][k])
    for k in range(len(grid)):
        cross.append(grid[k][j])
    return cross

def get_x(cross):
    return sum(cross)%6

def get_dir(x):
    if x == 0:
        return 'U', 'D'
    elif x == 1:
        return 'L', 'R'
    elif x == 2:
        return 'U', 'R'
    elif x == 3:
        return 'R', 'D'
    elif x == 4:
        return 'D', 'L'
    elif x == 5:
        return 'L', 'U'

def get_period(x, p):
    return p[x][0], p[x][1]

def get_new_grid(grid, p):
    new_grid = [[0]*len(grid[0]) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                cross = get_cross(grid, i, j)
                x