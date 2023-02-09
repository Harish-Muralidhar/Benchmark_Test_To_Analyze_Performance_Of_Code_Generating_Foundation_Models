'''

'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if s<1500:
        hra=0.1*s
        da=0.9*s
    else:
        hra=500
        da=0.98*s
    return s+hra+da

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = int(input())

        result = solve(s)

        fptr.write(str(result) + '\n')

    fptr.close()