"""

"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_cross(map):
    count = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == '^':
                l = r = t = b = 0
                for i in range(col - 1, -1, -1):
                    if map[row][i] == '#':
                        break
                    l += 1
                for i in range(col + 1, len(map[0])):
                    if map[row][i] == '#':
                        break
                    r += 1
                for i in range(row - 1, -1, -1):
                    if map[i][col] == '#':
                        break
                    t += 1
                for i in range(row + 1, len(map)):
                    if map[i][col] == '#':
                        break
                    b += 1
                min_len = min(l, r, t, b)
                if is_prime(min_len):
                    count += 1
    return count

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    map = []
    for _ in range(r):
        map.append(list(input()))
    print(find_prime_cross(map))