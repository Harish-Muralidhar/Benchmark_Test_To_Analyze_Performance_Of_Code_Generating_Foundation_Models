'''

'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, 2**n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += a[j]
        if not s & (1 << (m-1)):
            ans += 1
    print(ans % 1000000009)