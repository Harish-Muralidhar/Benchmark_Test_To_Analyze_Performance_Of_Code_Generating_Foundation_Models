'''


'''

import numpy as np

def broken_telephone(n, arr):
    count = 0
    for i in range(1, n-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(broken_telephone(n, arr))