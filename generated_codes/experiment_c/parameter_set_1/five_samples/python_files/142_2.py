'''

'''

def f(n, x, y, m=1000000007):
    if x == y:
        return 1 if x <= n else 0
    a, b = 0, 0
    if x < n:
        a = f(n, x, x) * f(n - x, x, y) % m
    if y < n:
        b = f(n, y, y) * f(n - y, x, y) % m
    if x == y + 1:
        r = (a + b) % m
    else:
        r = (a + b + f(n, x, y + 1) * f(n - y - 1, x, y)) % m
    return r

t = int(input())
for _ in range(t):
    n = int(input())
    a = [list(map(int,input().split())) for i in range(n)]
    x, y = min(a, key=lambda x:x[0])[0], max(a, key=lambda x:x[1])[1]
    s = ''
    for i in range(n):
        s += '1' if x <= a[i][1] else '0'
    print(f(n, x, y))
    print(s)