'''

'''


# Write your code here

import math
import os
import random
import re
import sys

# Complete the function below.

def countMishearAndWrongWhisper(A):
    print(A)
    out = 0
    for i in A:
        if(i!=A[0]):
            out = out + 1
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = countMishearAndWrongWhisper(A)

        fptr.write(str(result) + '\n')

    fptr.close()