"""
"""

import itertools

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    f = 0
    if s % x == 0:
        a = s // x
        for i in range(1, n+1):
            b = list(itertools.combinations(arr, i))
            for j in b:
                if sum(j) == a:
                    print(-1)
                    f = 1
                    break
            if f == 1:
                break
        if f == 0:
            print(a)
    else:
        print(-1)