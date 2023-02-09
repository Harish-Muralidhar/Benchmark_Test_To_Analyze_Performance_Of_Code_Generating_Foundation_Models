'''

'''

import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_cpc(i, j, r, c, grid):
    l = 0
    r = 0
    t = 0
    b = 0
    for k in range(j - 1, -1, -1):
        if grid[i][k] == '^':
            l += 1
        else:
            break
    for k in range(j + 1, c):
        if grid[i][k] == '^':
            r += 1
        else:
            break
    for k in range(i - 1, -1, -1):
        if grid[k][j] == '^':
            t += 1
        else:
            break
    for k in range(i + 1, r):
        if grid[k][j] == '^':
            b += 1
        else:
            break
    if min(l, r, t, b) == 0:
        return False
    return is_prime(min(l, r, t, b))

def get_cpc_count(r, c, grid):
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '^' and is_cpc(i, j, r, c, grid):
                count += 1
    return count

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(list(input().strip()))
    print(get_cpc_count(r, c, grid))