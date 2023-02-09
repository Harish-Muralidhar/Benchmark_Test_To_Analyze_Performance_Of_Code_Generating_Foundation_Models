"""

Note: This solution is by my brother Mr. Anand Kumar.
"""

import math
import os
import random
import re
import sys


# Complete the function below.
def lights(n):
    return int(math.sqrt(2 * n + 0.25) - 0.5)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()