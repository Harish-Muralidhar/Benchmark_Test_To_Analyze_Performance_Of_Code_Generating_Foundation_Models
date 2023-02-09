'''

Explanation
Example case 1.
There are no CPCs in the map.

Example case 2.
The map has 3 CPCs.

The first CPC is at (1, 3) and it can accommodate 2 monsters.
The second CPC is at (2, 5) and it can accommodate 1 monster.
The third CPC is at (3, 1) and it can accommodate 1 monster.

Hence, the total number of monsters is 3.

'''

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_cpc(x, y, grid):
    l = 0
    r = 0
    t = 0
    b = 0
    for i in range(x - 1, -1, -1):
        if grid[i][y] == '^':
            l += 1
        else:
            break
    for i in range(x + 1, len(grid)):
        if grid[i][y] == '^':
            b += 1
        else:
            break
    for i in range(y - 1, -1, -1):
        if grid[x][i] == '^':
            t += 1
        else:
            break
    for i in range(y + 1, len(grid[0])):
        if grid[x][i] == '^':
            r += 1
        else:
            break
    m = min(l, r, t, b)
    count = 0
    for i in range(1, m + 1):
        if is_prime(i):
            count += 1
    return count

def count_monsters(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                count += is_cpc(i, j, grid)
    return count

def main():
    t