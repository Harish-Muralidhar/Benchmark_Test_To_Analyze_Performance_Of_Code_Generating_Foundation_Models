'''

'''

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_cpc(x, y, arr):
    l = 0
    r = 0
    t = 0
    b = 0
    for i in range(x - 1, -1, -1):
        if arr[i][y] == '^':
            t += 1
        else:
            break
    for i in range(x + 1, len(arr)):
        if arr[i][y] == '^':
            b += 1
        else:
            break
    for i in range(y - 1, -1, -1):
        if arr[x][i] == '^':
            l += 1
        else:
            break
    for i in range(y + 1, len(arr[0])):
        if arr[x][i] == '^':
            r += 1
        else:
            break
    if min(l, r, t, b) == 0:
        return False
    for i in range(2, min(l, r, t, b) + 1):
        if is_prime(i):
            return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        arr = []
        for i in range(r):
            arr.append(list(input()))
        count = 0
        for i in range(r):
            for j in range(c):
                if arr[i][j] == '^' and is_cpc(i, j, arr):
                    count += 1
        print(count)

main()