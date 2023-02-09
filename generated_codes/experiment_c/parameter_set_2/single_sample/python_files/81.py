'''




'''

import sys

def dR(P,t):
    A = 0
    B = 0
    for i in range(t):
        if P[i] == 'A':
            A += 1
        else:
            B += 1
    return A-B

def dS(P):
    return max(dR(P,i) for i in range(len(P)))

def dT(P):
    return max(dR(P,i) for i in range(len(P)))

def dST(P):
    return max(dS(P),dT(P))

def solve(S,T):
    n = len(S)
    P = ['A']*n
    for i in range(n):
        if dST(P) > dST(P[:S[i]]+['B']+P[S[i]+1:]):
            P[S[i]] = 'B'
    return ''.join(P)

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        n = int(sys.stdin.readline())
        S = [int(x) for x in sys.stdin.readline().split()]
        T = [int(x) for x in sys.stdin.readline().split()]
        print(solve(S,T))

if __name__ == '__main__':
    main()