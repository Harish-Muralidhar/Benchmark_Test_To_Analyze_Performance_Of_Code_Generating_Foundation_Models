"""

Test data is such that the number of guns to be destroyed is smaller than 232.

Explanation

The only rocks are located at the points (0, 0) and (0, 1).

The line connecting your cannon and (0, 2) is free of rocks, so you can fire at that gun.

The line connecting your cannon and (1, 2) passes through the rock located at (0, 0),
so you cannot fire at that gun.

The line connecting your cannon and (-2, 2) passes through the rock located at (0, 1),
so you cannot fire at that gun.

The line connecting your cannon and (-1, 2) is free of rocks, so you can fire at that gun.

Hence you can destroy 2 out of the 3 guns.
"""

from math import floor
from math import ceil
from fractions import gcd
from fractions import Fraction

def main():
    n = int(input())
    for i in range(n):
        y, x1, x2 = map(int, input().split())
        d = gcd(x1, y)
        if d == 1:
            print(x2 - x1 + 1)
        else:
            p = floor(Fraction(x1, y))
            q = ceil(Fraction(x2, y))
            print(q - p + 1)

main()