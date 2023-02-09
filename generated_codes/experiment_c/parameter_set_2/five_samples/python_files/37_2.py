"""


"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m, k):
    if abs(n-m)<=k:
        return 0
    elif n>m:
        return n-m-k
    else:
        return m-n-k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nmk = input().split()

        n = int(nmk[0])

        m = int(nmk[1])

        k = int(nmk[2])

        result = solve(n, m, k)

        fptr.write(str(result) + '\n')

    fptr.close()