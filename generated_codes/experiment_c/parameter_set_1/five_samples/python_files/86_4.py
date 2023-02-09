'''

'''

def numberOfWays(n, m, sx, sy, fx, fy, h):
    if (sx == fx and sy == fy):
        if (h[fx][fy] == 1):
            return 1
        return 0
    result = 0
    if (h[fx][fy] == 1):
        return result
    if (fx + 1 < n):
        if (h[fx + 1][fy] > 0):
            h[fx + 1][fy] -= 1
            result += numberOfWays(n, m, sx, sy, fx + 1, fy, h)
            h[fx + 1][fy] += 1
    if (fx - 1 >= 0):
        if (h[fx - 1][fy] > 0):
            h[fx - 1][fy] -= 1
            result += numberOfWays(n, m, sx, sy, fx - 1, fy, h)
            h[fx - 1][fy] += 1
    if (fy - 1 >= 0):
        if (h[fx][fy - 1] > 0):
            h[fx][fy - 1] -= 1
            result += numberOfWays(n, m, sx, sy, fx, fy - 1, h)
            h[fx][fy - 1] += 1
    if (fy + 1 < m):
        if (h[fx][fy + 1] > 0):
            h[fx][fy + 1] -= 1
            result += numberOfWays(n, m, sx, sy, fx, fy + 1, h)
            h[fx][fy + 1] += 1
    if (fx + 2 < n):
        if (h[fx + 2][fy] > 0):
            h[fx + 2][fy] -= 1
            result += numberOfWays(n, m, sx, sy, fx + 2, fy, h)
            h[fx + 2][fy] += 1
    if (fx - 2 >= 0):
        if (h[fx - 2][fy] > 0):
            h[fx - 2][fy] -= 1
            result += numberOfWays(n, m, sx, sy, fx - 2, fy, h)
            h[fx - 2][fy] += 1
    if (fy - 2 >= 0):
        if (h[fx][fy - 2] > 0):
            h[fx][fy - 2] -= 1
            result += numberOfWays(n, m, sx, sy, fx, fy - 2, h)
            h[fx][fy - 2] += 1
    if (fy + 2 < m):
        if (h[fx][fy + 2] > 0):
            h[fx][fy + 2] -= 1
            result += numberOfWays(n, m, sx, sy, fx, fy + 2, h)
            h[fx][fy + 2] += 1
    return result

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    h = []
    for j in range(n):
        h.append(list(map(int, input().split())))
    print(numberOfWays(n, m, sx, sy, fx, fy, h))