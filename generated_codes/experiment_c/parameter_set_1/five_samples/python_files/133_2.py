"""
 pair.
Case 4 : N = 6. Arjuna can make the pair (1,3) and Bhima can make the pair (2,4). No matter which order they choose, they can make 2 pairs without crossing each other.
"""

import numpy as np

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def isEven(n):
    return n % 2 == 0

def whoWin(n):
    if isPrime(n):
        return 'Bhima'
    if isEven(n):
        return 'Arjuna'
    else:
        return 'Bhima'

T = int(input())
for i in range(T):
    N = int(input())
    print(whoWin(N))