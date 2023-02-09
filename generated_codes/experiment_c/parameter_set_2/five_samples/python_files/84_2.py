"""

"""

# SOLUTION

import math

def binomial_coeff(n, k): 
    res = 1
    if (k > n - k): 
        k = n - k 
    for i in range(0 , k): 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 

def find_moves(r, c, g):
    moves = []
    while(g > 0):
        if(c == 0):
            break
        if(r >= c):
            moves.append(binomial_coeff(r, c))
            g -= binomial_coeff(r, c)
            r -= 1
        c -= 1
    return len(moves), moves

t = int(input())
for _ in range(t):
    r, c, g = map(int, input().split())
    k, moves = find_moves(r, c, g)
    print(k)
    print(*moves)