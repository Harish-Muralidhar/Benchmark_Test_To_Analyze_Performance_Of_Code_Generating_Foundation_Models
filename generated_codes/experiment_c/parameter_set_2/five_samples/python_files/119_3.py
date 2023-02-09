"""


"""

import math

def is_possible(n):
    if n == 1:
        return "y y y"
    elif n == 2:
        return "n y y"
    else:
        if n % 2 == 0:
            return "y y n"
        else:
            return "n y n"

t = int(input())
for i in range(t):
    n = int(input())
    print(is_possible(n))