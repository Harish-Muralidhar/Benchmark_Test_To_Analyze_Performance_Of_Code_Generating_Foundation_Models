'''
'''

import math
import os
import random
import re
import sys

#
# Complete the 'minimumScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY p
#  3. INTEGER k
#  4. INTEGER m
#

def minimumScore(a, p, k, m):
    # Write your code here
    Sum = 0
    for i in range(len(p)):
        Sum += p[i]
    Sum += 1
    for i in range(len(a)):
        Sum += a[i]
    Sum = round(Sum/k)
    print(Sum)
    if(Sum < m):
        return m
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        e = int(first_multiple_input[2])

        m = int(first_multiple_input[3])

        a = []

        for _ in range(n-1):
            a.append(list(map(int, input().rstrip().split())))

        p = list(map(int, input().rstrip().split()))

        result = minimumScore(a, p, k, m)

        fptr.write(str(result) + '\n')

    fptr.close()