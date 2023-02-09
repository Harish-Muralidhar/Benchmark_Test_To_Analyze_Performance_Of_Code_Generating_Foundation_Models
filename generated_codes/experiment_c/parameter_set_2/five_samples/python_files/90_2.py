"""


Sample Input

4 3 1 4
1 3 5
3 3 4
2 2 1
2 1 2

Sample Output

2

Explanation

The optimal solution is to remove the barricades at (2,2) and (2,1) for a total cost of 2.
"""

import math
import sys

def main():
    input_data = sys.stdin.readlines()
    w, h, d, n = [int(x) for x in input_data[0].split()]
    barricades = []
    for i in range(1, n+1):
        barricades.append([int(x) for x in input_data[i].split()])

    #print(w, h, d, n)
    #print(barricades)

    # find the center of the square
    # the center is the midpoint of the diagonal
    # the diagonal is parallel to the axes
    # the diagonal is 2d long
    # the center is at an integer coordinate
    # the center is at (x,y)
    # the center is at (x + d, y + d)
    # the center is at (x - d, y - d)
    # the center is at (x + d, y - d)
    # the center is at (x - d, y + d)
    # the center is at (x, y + d)
    # the center is at (x, y - d)
    # the center is at (x + d, y)
    # the center is at (x - d, y)
    # the center is at (w/2, h/2)
    # the center is at (w/2 + d, h/2 + d)
    # the center is at (w/2 - d, h/2 - d)
    # the center is at (w/2 + d, h/2 - d)
    # the center is at (w/2 - d, h/2 + d)
    # the center is at (w/2, h/2 + d)
    # the center is at (w/2, h/2 - d