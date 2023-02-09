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
@.D..

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
@D...

Output:
0



Example 5


Input:
7 5
....$
.....
.....
D...D
.....
.....
@DD..

Output:
0

'''

import numpy as np

def find_chef(map):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i][j] == '@':
                return i,j

def find_spagetti(map):
    spagetti = []
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i][j] == 'D':
                spagetti.append((i,j))
    return spagetti

def find_spoon(map):
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i][j] == '$':
                return i,j

def find_distance(map,chef,spagetti):
    dist = []
    for i in range(len(spagetti)):
        dist.append(abs(spagetti[i][0] - chef[0]) + abs(spagetti[i][1] - chef[1]))
    return min(dist)

def find_distance_spoon(map,chef,spoon):
    return abs(spoon[0] - chef[0]) + abs(spoon[1] - chef[1])

def main():
    n,m = map(int,input().split())
    map = []
    for i in range(n):
        map.append(list(input()))
    map = np.array(map)
    chef = find_che