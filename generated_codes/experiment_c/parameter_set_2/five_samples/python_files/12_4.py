"""


"""

import sys

def min_rooms_to_paint(s):
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    return min(r, g, b)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(min_rooms_to_paint(s))