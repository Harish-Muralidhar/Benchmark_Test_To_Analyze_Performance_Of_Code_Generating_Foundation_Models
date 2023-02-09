'''


'''

import math
import os
import random
import re
import sys

def solve(A):
    N = len(A)
    y = [-1] * N
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] == 0:
                y[i] = 0
                y[j] = 0
                break
        if y[i] == 0:
            break
    if y[i] == 0:
        return y
    for i in range(N):
        if y[i] == -1:
            y[i] = 1
    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = []

        for _ in range(n):
            A.append(list(map(int, input().rstrip().split())))

        result = solve(A)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()