'''
 pairs ( without crossing the pair made by Bhima )
Case 4 : N = 6. Arjuna can make the pair (1,4) and Bhima can not make any more pairs ( without crossing the pair (1,4) )

'''

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def winner(n):
    if n == 2:
        return "Arjuna"
    if n % 2 == 0:
        return "Arjuna"
    if is_prime(n):
        return "Bhima"
    return "Arjuna"

t = int(input())
for _ in range(t):
    n = int(input())
    print(winner(n))