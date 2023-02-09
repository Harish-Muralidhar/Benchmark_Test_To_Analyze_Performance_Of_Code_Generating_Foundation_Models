'''

'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n):
    if n < 10:
        return n
    else:
        return n % 10 + solve(n // 10)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()