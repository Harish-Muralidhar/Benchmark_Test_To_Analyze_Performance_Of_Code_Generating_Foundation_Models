'''

Explanation
Example case 1. There are no CPCs in the map.
Example case 2. There are 3 CPCs in the map.

The first CPC is at (1, 1), with P = 2.
The second CPC is at (3, 8), with P = 5.
The third CPC is at (5, 4), with P = 3.

'''

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def get_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return i
    return n

def get_num_monsters(arr, r, c):
    num_monsters = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '^':
                l = 0
                r = 0
                t = 0
                b = 0
                for k in range(j, c):
                    if arr[i][k] == '^':
                        r += 1
                    else:
                        break
                for k in range(j, -1, -1):
                    if arr[i][k] == '^':
                        l += 1
                    else:
                        break
                for k in range(i, r):
                    if arr[k][j] == '^':
                        b += 1
                    else:
                        break
                for k in range(i, -1, -1):
                    if arr[k][j] == '^':
                        t += 1
                    else:
                        break
                min_val = min(l, r, t, b)
                num_primes = 0
                for k in range(2, min_val+1):
                    if is_prime(k):
                        num_primes += 1
                num_monsters += num_primes
