'''

'''

import math

def binomial_coefficient(n,k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def bico_grid(r,c,g):
    if g == 0:
        return [0]
    if g < 0:
        return [0,0]
    if r == 0:
        return [0,0]
    if c == 0:
        return [0,0]
    if c > r:
        return [0,0]
    if g > binomial_coefficient(r,c):
        return [0,0]
    if g == binomial_coefficient(r,c):
        return [1,g]
    if g < binomial_coefficient(r,c):
        return [2,g,binomial_coefficient(r,c) - g]

t = int(input())
for i in range(t):
    r,c,g = map(int,input().split())
    result = bico_grid(r,c,g)
    print(result[0])
    print(*result[1:])