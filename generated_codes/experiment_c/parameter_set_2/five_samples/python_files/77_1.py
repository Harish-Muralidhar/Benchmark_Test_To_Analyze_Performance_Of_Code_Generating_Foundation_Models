'''

Example 3


Input:
7 5
....$
.....
.....
D...D
.....
.....
@DDDD

Output:
1



Example 4


Input:
7 5
....$
.....
.....
D...D
.....
.....
@..DD

Output:
1



Example 5


Input:
7 5
....$
.....
.....
D...D
.....
.....
@.DDD

Output:
2

'''

import numpy as np

def find_neighbours(i, j, n, m):
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < n-1:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < m-1:
        neighbours.append((i, j+1))
    if i > 0 and j > 0:
        neighbours.append((i-1, j-1))
    if i > 0 and j < m-1:
        neighbours.append((i-1, j+1))
    if i < n-1 and j > 0:
        neighbours.append((i+1, j-1))
    if i < n-1 and j < m-1:
        neighbours.append((i+1, j+1))
    return neighbours

def find_distance(i, j, n, m, arr):
    arr[i][j] = 0
    neighbours = find_neighbours(i, j, n, m)
    for neighbour in neighbours:
        if arr[neighbour[0]][neighbour[1]] == '.':
            arr[neighbour[0]][neighbour[1]] = arr[i][j] + 1
            find_distance(neighbour[0], neighbour[1], n, m, arr)
    return arr

def find_min_distance(arr, n, m):
    min_distance = n*m
    for i in range(n):
        for