'''

'''

import math
import os
import random
import re
import sys

# Complete the function below.

def solve(a, b):
    n=len(a)
    count=0
    for i in range(n):
        if (b[i]<=(a[i]-a[i-1])) and (i==0):
            count+=1
        elif (b[i]<=(a[i]-a[i-1])) and (i!=0):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()