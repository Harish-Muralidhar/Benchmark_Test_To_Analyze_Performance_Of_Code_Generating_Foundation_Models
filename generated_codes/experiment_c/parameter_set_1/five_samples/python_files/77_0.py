'''

Example 3


Input:
7 5
....$
.....
.....
.DDD.
.....
.....
@....

Output:
1



Example 4


Input:
7 5
@....
.....
.....
D...D
.....
.....
....$

Output:
2



Example 5


Input:
7 5
@....
.....
.....
.DDD.
.....
.....
....$

Output:
1
'''

#Solution:

import sys
import queue
import heapq

def eat(x):
    if x[0] == 'D': 
        return True
    if x[0] == '@': 
        return False
    if x[0] == '$':
        return False
    return None


def trans(x):
    if x[0] == 'D': 
        return 'D'
    if x[0] == '@': 
        return '@'
    if x[0] == '$':
        return '$'
    if x[0] == '.':
        return '.'
    return None

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def get_eat(grid, start, end, monster_pos):
    if eat(start) == False and eat(end) == None:
        return 0
    if start == end:
        return 0
    if eat(start) == None and eat(end) == False:
        return distance(start, end)
    if eat(start) == eat(end):
        return 0
    if eat(start) == True and eat(end) == False:
        visited = set()
        q = []
        heapq.heappush(q, (0, end))
        while q:
            curr = heapq.heappop(q)
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            if eat(grid[curr[1][0]][curr[1][1]]) == True and distance(curr[1], end) <= 2:
                visited.clear()
                return distance(curr[1], start)
            for n in neighbors(grid, curr[1]):
                if eat(grid[n[0]][n[1]]) == False:
                    heapq.heappush(q, (curr[0] + 1, n))
        return 1000000
    if eat(start) == False and eat(end) == True:
        visited = set()
        q = []
        heapq.heappush(q, (0, start))
        while q:
            curr = heapq.heappop(q)
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            if eat(grid[curr[1][0]][curr[1][1]]) == True and distance(curr[1], end) <= 2:
                visited.clear()
                return distance(curr[1], start)
            for n in neighbors(grid, curr[1]):
                if eat(grid[n[0]][n[1]]) == False:
                    heapq.heappush(q, (curr[0] + 1, n))
        return 1000000


def neighbors(grid, curr):
    h = len(grid)
    w = len(grid[0])
    ret = []
    if curr[0] > 0:
        ret.append((curr[0] - 1, curr[1]))
        if curr[1] > 0:
            ret.append((curr[0] - 1, curr[1] - 1))
        if curr[1] < w - 1:
            ret.append((curr[0] - 1, curr[1] + 1))
    if curr[0] < h - 1:
        ret.append((curr[0] + 1, curr[1]))
        if curr[1] > 0:
            ret.append((curr[0] + 1, curr[1] - 1))
        if curr[1] < w - 1:
            ret.append((curr[0] + 1, curr[1] + 1))
    if curr[1] > 0:
        ret.append((curr[0], curr[1] - 1))
    if curr[1] < w - 1:
        ret.append((curr[0], curr[1] + 1))
    return ret

def compute(grid):
    h = len(grid)
    w = len(grid[0])
    monster_pos = []
    start = None
    end = None
    for i in range(h):
        for j in range(w):
            if trans(grid[i][j]) == '@':
                start = (i, j)
            if trans(grid[i][j]) == '$':
                end = (i, j)
            if trans(grid[i][j]) == 'D':
                monster_pos.append((i, j))
    return get_eat(grid, start, end, monster_pos)

def main():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    arr = list(map(int, input().split()))
    grid = []
    h = arr[0]
    w = arr[1]
    for i in range(h):
        grid.append(list(input()))
    print(compute(grid))


if __name__ == '__main__':
    main()