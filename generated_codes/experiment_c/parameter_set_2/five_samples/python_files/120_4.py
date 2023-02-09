'''

'''

import numpy as np

def prob_matrix(n,m):
    P = np.zeros((n,m))
    P[0][0] = 1
    for i in range(1,n):
        P[i][0] = P[i-1][0]/2
    for j in range(1,m):
        P[0][j] = P[0][j-1]/2
    for i in range(1,n):
        for j in range(1,m):
            P[i][j] = (P[i][j-1] + P[i-1][j])/2
    return P

def sum_prob(P,n,m):
    return np.sum(P[:n,:m])

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        P = prob_matrix(n,m)
        print(sum_prob(P,n,m))