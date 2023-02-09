'''

Explanation
Example case 1: Joe can play the beat notation (2, 5, 8, 11) while Chef can play the beat notation (4, 8, 16).
Example case 2: Joe can play the beat notation (2, 3, 4, 5) while Chef can play the beat notation (1, 2, 4).
Example case 3: Joe can play the beat notation (2, 3, 9, 10, 19, 27, 28, 81) while Chef can play the beat notation (1, 3, 9, 27, 81).
Example case 4: Joe can play the beat notation (2, 4, 7, 10, 13, 25) while Chef can play the beat notation (1, 4, 7, 10, 25).

'''

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def get_arithmetic_progression(a, b, n):
    d = (b - a) // (n - 1)
    return [a + d * i for i in range(n)]

def get_geometric_progression(a, b, n):
    r = math.pow(b / a, 1 / (n - 1))
    return [int(a * math.pow(r, i)) for i in range(n)]

def get_arigeom_progression(a, b, n):
    if n == 2:
        return [a, b]
    if n == 3:
        return [a, b, a + b]
    if n == 4:
        return [a, b, a + b, 2 * b]
    if n == 5:
        return [a, b, a + b, 2 * b, a + 2 * b]
    if n == 6:
        return [a, b, a + b, 2 * b, a + 2 * b, 3 * b]
    if n == 7:
        return [a, b, a + b, 2 * b, a + 2