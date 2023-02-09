"""


"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n):
    if n==1:
        return 2
    else:
        return (n*2)-1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()