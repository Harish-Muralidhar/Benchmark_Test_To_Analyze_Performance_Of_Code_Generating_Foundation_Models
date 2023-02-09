'''

'''

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def ways(n):
    return nCr(n,2) + nCr(n,1)

T = int(input())
for _ in range(T):
    N = int(input())
    print(int(ways(N))%1000000007)