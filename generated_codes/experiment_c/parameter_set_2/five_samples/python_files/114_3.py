'''

'''

import numpy as np

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for i in range(q):
    k = int(input())
    arr_sorted = np.sort(arr)
    arr_sorted = arr_sorted[::-1]
    cost = 0
    for j in range(n):
        if j % (k+1) == 0:
            cost += arr_sorted[j]
    print(cost)