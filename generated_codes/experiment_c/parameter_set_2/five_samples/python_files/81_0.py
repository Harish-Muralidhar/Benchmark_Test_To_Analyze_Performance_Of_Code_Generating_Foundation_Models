"""




"""

import sys

def dR(P,t):
    return abs(P[:t].count('A') - P[:t].count('B'))

def dS(P):
    return max([dR(P,t) for t in range(1,len(P)+1)])

def dT(P):
    return max([dR(P[::-1],t) for t in range(1,len(P)+1)])

def solve(n,S,T):
    P = []
    for i in range(n):
        if S[i] == T[i]:
            if i%2 == 0:
                P.append('A')
            else:
                P.append('B')
        else:
            if dR(P,i) > dR(P[::-1],i):
                P.append('A')
            else:
                P.append('B')
    return ''.join(P)

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        n = int(sys.stdin.readline())
        S = [int(x) for x in sys.stdin.readline().split()]
        T = [int(x) for x in sys.stdin.readline().split()]
        print(solve(n,S,T))

if __name__ == '__main__':
    main()