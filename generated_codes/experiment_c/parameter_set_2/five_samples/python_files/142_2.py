"""

"""

import math

def solve(n, a, b):
    # Write your code here
    # print(n, a, b)
    if n == 1:
        if a[0] == 0 and b[0] == 0:
            return 1, "0"
        elif a[0] == 1 and b[0] == 1:
            return 1, "1"
        else:
            return 2, "01"
    else:
        if a[0] == 0 and b[0] == 0:
            return solve(n-1, a[1:], b[1:])
        elif a[0] == n and b[0] == n:
            return solve(n-1, a[1:], b[1:])
        else:
            left = solve(n-1, a[1:], b[1:])
            right = solve(n-1, [a[0]-1]+a[1:], [b[0]-1]+b[1:])
            return left[0]*right[0], left[1]+right[1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            ai, bi = map(int, input().split())
            a.append(ai)
            b.append(bi)
        ans = solve(n, a, b)
        print(ans[0])
        print(ans[1])