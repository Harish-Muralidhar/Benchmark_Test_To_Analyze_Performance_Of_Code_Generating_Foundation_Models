"""
"""

import itertools as it

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    l = len(arr)
    for j in range(1, l):
        for k in range(0, l-j):
            arr[k] = arr[k]+arr[k+1]
    arr = arr[l-n:l]
    print(*arr)