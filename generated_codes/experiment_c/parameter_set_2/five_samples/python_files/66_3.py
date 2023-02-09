'''

'''

import math

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

t = int(input())
for i in range(t):
    n = int(input())
    p = 1
    q = 10
    g = gcd(p,q)
    print(p//g,q//g)