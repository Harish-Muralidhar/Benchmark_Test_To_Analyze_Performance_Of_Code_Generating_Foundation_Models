'''

'''


import math
import os
import random
import re
import sys

#
# Complete the 'berlandPancakes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def berlandPancakes(a, b):
    # Write your code here
    count = 0
    for i in range(len(a)):
        if a[i] >= b[i]:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = berlandPancakes(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()