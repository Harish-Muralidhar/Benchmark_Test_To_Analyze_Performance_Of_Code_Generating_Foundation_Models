"""


"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m, q, sx, sy, p1, p2):
    # Return an array of integers representing the answer to all of the queries.
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmq = input().split()

    n = int(nmq[0])

    m = int(nmq[1])

    q = int(nmq[2])

    sxsy = input().split()

    sx = int(sxsy[0])

    sy = int(sxsy[1])

    p1 = list(map(int, input().rstrip().split()))

    p2 = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(n, m, q, sx, sy, p1, p2)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()