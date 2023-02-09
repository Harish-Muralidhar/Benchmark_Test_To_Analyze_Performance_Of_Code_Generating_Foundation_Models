'''

'''

import sys

def getMinimumCost(arr, k):
    n = len(arr)
    if k >= n:
        return sum(arr)
    arr.sort(reverse=True)
    total = 0
    for i in range(n):
        total += arr[i] * (1 + i // k)
    return total

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    k = int(input())
    print(getMinimumCost(arr, k))