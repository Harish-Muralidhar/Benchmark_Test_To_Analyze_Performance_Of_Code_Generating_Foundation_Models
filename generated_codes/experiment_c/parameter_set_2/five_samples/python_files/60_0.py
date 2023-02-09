'''


'''

import numpy as np

def solve(A, N):
    X = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                X[i][j] = 1
            else:
                X[i][j] = 0
    for i in range(N):
        for j in range(N):
            if X[i][j] == 1:
                X[i][j] = 0
            else:
                X[i][j] = 1
    return X

T = int(input())
for _ in range(T):
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    A = np.array(A)
    X = solve(A, N)
    if np.array_equal(X, np.zeros((N, N))):
        print(-1)
    else:
        for i in range(N):
            for j in range(N):
                print(int(X[i][j]), end=' ')
        print()