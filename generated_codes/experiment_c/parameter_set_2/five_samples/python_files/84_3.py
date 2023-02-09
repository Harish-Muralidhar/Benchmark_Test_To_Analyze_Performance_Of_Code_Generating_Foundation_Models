'''

'''

#code

import math

def binomial(n,k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

t = int(input())

for i in range(t):
    r,c,g = map(int,input().split())
    ans = []
    while(c>=0):
        ans.append(binomial(r,c))
        g -= binomial(r,c)
        r -= 1
        c -= 1
    print(len(ans))
    print(*ans)