'''

Explanation

In the given test case, the enemy battleship is located at the points (-2, 2), (-1, 2), (0, 2), and (1, 2).

Your cannon can destroy the guns at (-2, 2) and (1, 2) because the line connecting your cannon and those guns do not go through any rocks.

However, the line connecting your cannon and the guns at (-1, 2) and (0, 2) go through the rock at (0, 0).

Thus, you can only destroy two of the four guns.

'''

import math
import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def count_guns(y, x1, x2):
    count = 0
    for i in range(x1, x2+1):
        if gcd(abs(i), abs(y)) == 1:
            count += 1
    return count

def main():
    t = int(input())
    for i in range(t):
        y, x1, x2 = map(int, input().split())
        print(count_guns(y, x1, x2))

if __name__ == '__main__':
    main()