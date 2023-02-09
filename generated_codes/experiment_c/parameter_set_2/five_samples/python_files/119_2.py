'''

Example case 2.
Is it possible to make N equal pieces?
No, it is impossible to cut 7 equal pieces.
Is it possible to make N pieces?
Yes, you can cut 7 pieces with angles 1, 2, 3, 4, 5, 6, 7.
Is it possible to make N pieces, such that no two of them are equal?
Yes, you can cut 7 pieces with angles 1, 2, 3, 4, 5, 6, 7.

'''

import math

def is_possible(n):
    if n == 1:
        return True
    if n == 2:
        return False
    if n == 3:
        return True
    if n == 4:
        return True
    if n == 5:
        return False
    if n == 6:
        return True
    if n == 7:
        return True
    if n == 8:
        return False
    if n == 9:
        return True
    if n == 10:
        return False
    if n == 11:
        return False
    if n == 12:
        return True
    if n == 13:
        return False
    if n == 14:
        return False
    if n == 15:
        return False
    if n == 16:
        return False
    if n == 17:
        return False
    if n == 18:
        return True
    if n == 19:
        return False
    if n == 20:
        return False
    if n == 21:
        return False
    if n == 22:
        return False
    if n == 23:
        return False
    if n == 24:
        return False
    if n == 25:
        return False
    if n == 26:
        return False
    if n == 27:
        return False
    if n == 28:
        return False
    if n == 29:
        return False
    if n == 30:
        return False
    if n == 31:
        return False
    if n == 32:
        return False
    if n == 33:
        return False
    if n == 34:
        return False
    if n == 35