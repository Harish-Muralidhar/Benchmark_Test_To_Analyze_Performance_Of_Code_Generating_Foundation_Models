'''

'''

import math

def notes(n):
    d = [1, 2, 5, 10, 50, 100]
    c = 0
    for i in range(len(d)):
        if n//d[i] != 0:
            c += (n//d[i])
            n = n%d[i]
    print(c)

t = int(input())
for i in range(t):
    n = int(input())
    notes(n)