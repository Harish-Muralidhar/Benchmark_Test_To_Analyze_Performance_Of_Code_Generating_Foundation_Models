'''

'''

import math
import os
import random
import re
import sys

# Complete the function below.

def foo(n, arr):
    even=0
    odd=0
    for i in arr:
        if i%2==0:
            even=even+1
        else:
            odd+=1
    if even>odd:
        return "READY FOR BATTLE"
    else:
        return "NOT READY"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = foo(n, arr)

    fptr.write(result + '\n')

    fptr.close()