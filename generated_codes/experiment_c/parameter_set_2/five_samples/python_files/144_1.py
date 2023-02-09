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

def get_count(grid, r, c):
    count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '#':
                continue
            l = r_ = t = b = 0
            for k in range(j - 1, -1, -1):
                if grid[i][k] == '#':
                    break
                l += 1
            for k in range(j + 1, c):
                if grid[i][k] == '#':
                    break
                r_ += 1
            for k in range(i - 1, -1, -1):
                if grid[k][j] == '#':
                    break
                t += 1
            for k in range(i + 1, r):
                if grid[k][j] == '#':
                    break
                b += 1
            if is_prime(min(l, r_, t, b)):
                count += 1
    return count

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    grid = []
    for i in range(r):
        grid.append(list(input()))
    print(get_count(grid, r, c))