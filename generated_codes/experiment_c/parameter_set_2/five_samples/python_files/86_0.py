'''


'''

import math

def ways(n, m, sx, sy, fx, fy):
    if sx == fx and sy == fy:
        return 1
    if sx < 1 or sy < 1 or sx > n or sy > m:
        return 0
    return ways(n, m, sx + 1, sy, fx, fy) + ways(n, m, sx - 1, sy, fx, fy) + ways(n, m, sx, sy + 1, fx, fy) + ways(n, m, sx, sy - 1, fx, fy) + ways(n, m, sx + 2, sy, fx, fy) + ways(n, m, sx - 2, sy, fx, fy) + ways(n, m, sx, sy + 2, fx, fy) + ways(n, m, sx, sy - 2, fx, fy)


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(ways(n, m, sx, sy, fx, fy))