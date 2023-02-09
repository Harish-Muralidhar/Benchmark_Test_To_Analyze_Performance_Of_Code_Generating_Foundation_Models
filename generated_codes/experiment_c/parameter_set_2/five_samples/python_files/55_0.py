"""

"""

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_list(l):
    if len(l) == 0:
        return 1
    g = l[0]
    for i in range(1, len(l)):
        g = gcd(g, l[i])
    return g

def product_of_gcd(l):
    n = len(l)
    p = 1
    for i in range(1, 2 ** n):
        s = []
        for j in range(n):
            if i & (1 << j):
                s.append(l[j])
        p = (p * gcd_list(s)) % 1000000007
    return p

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(product_of_gcd(l))