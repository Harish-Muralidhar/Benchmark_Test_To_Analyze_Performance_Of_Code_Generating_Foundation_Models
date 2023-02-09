"""

"""

#Solution

import sys

def solve(n, a, b):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[j] += dp[j - 1]
            dp[j] %= mod
    return dp[n]

mod = 1000000007

for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(solve(n, a, b))
    print(''.join('1' if i == n else '0' for i in a))