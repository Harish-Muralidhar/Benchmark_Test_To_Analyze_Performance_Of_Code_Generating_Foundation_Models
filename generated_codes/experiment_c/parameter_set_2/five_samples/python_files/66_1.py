'''

'''

import math

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def find_prob(n):
    p = 1
    q = 10
    if n<=10:
        p = n
    else:
        p = 10
    g = gcd(p,q)
    p = p//g
    q = q//g
    print(p,q)

t = int(input())
for i in range(t):
    n = int(input())
    find_prob(n)