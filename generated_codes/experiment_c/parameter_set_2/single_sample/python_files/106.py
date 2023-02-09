'''


'''

# Write your code here

import numpy as np

def update(a, i, v):
    a[i] += v
    a[i] %= M

def update_range(a, i, j, v):
    for k in range(i, j+1):
        a[k] *= v
        a[k] %= M

def update_range_init(a, i, j, v):
    for k in range(i, j+1):
        a[k] = v

def sum_range(a, i, j):
    return sum(a[i:j+1])

N, Q = map(int, input().split())
A = list(map(int, input().split()))

M = 10**9 + 7

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update_range(A, q[1]-1, q[2]-1, q[3])
    elif q[0] == 2:
        update_range(A, q[1]-1, q[2]-1, q[3])
    elif q[0] == 3:
        update_range_init(A, q[1]-1, q[2]-1, q[3])
    elif q[0] == 4:
        print(sum_range(A, q[1]-1, q[2]-1) % M)