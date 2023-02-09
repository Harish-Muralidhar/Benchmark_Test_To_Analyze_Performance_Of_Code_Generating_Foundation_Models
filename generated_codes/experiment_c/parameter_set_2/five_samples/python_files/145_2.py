"""

Explanation
Example case 1.
There are no CPCs in the map.

Example case 2.
There are three CPCs in the map.

CPC 1: (1, 1)
L = 3, R = 3, T = 3, B = 3
Possible primes are 2 and 3.

CPC 2: (3, 5)
L = 2, R = 2, T = 2, B = 2
Possible primes are 2 and 3.

CPC 3: (4, 6)
L = 2, R = 2, T = 2, B = 2
Possible primes are 2 and 3.

Since each CPC can accommodate 2 monsters, the map can accommodate 3 monsters.

"""

import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

def isCPC(i, j, r, c, a):
    l = 0
    rr = 0
    t = 0
    b = 0
    for k in range(j - 1, -1, -1):
        if a[i][k] == '#':
            break
        l += 1
    for k in range(j + 1, c):
        if a[i][k] == '#':
            break
        rr += 1
    for k in range(i - 1, -1, -1):
        if a[k][j] == '#':
            break
        t += 1
    for k in range(i + 1, r):
        if a[k][j] == '#':
            break
        b += 1
    m = min(l, rr, t, b)
    count = 0
    for k in range(2, m + 1):
        if isPrime(k):
            count += 1
    return