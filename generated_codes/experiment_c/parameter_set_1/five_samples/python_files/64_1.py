'''
In the third case they are (2,0,0,0,0) and (1,1,0,0,0).

'''
import math

M = 1000000009


def solve(n, k):
    if k == 1:
        return 1
    ans = 0
    for i in range(1, 2 ** k - 1):
        a1 = n - i
        a2 = i
        if a1 < 0 or a2 < 0:
            continue
        ans += (math.factorial(n - 1) // (math.factorial(a1) * math.factorial(a2))) % M
        ans %= M
    return ans


t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    print(solve(n, k))