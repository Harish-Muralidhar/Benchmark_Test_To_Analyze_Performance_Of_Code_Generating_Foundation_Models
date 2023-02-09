"""
"""

import math

t = int(input())

for i in range(t):
    n = int(input())
    z = 0

    count = 0
    while n/5 > 0:
        z = z + math.floor(n/5)
        n = n/5
    print(int(z))