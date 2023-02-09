'''

'''

import math

def binomial(n,k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

def bico_grid(R,C,G):
    if(R<C):
        C,R=R,C
    if(G<=binomial(R,C)):
        return [C,G]
    else:
        G-=binomial(R,C)
        return [C]+bico_grid(R-1,C-1,G)

T=int(input())
for _ in range(T):
    R,C,G=map(int,input().split())
    result=bico_grid(R,C,G)
    print(len(result))
    print(*result)