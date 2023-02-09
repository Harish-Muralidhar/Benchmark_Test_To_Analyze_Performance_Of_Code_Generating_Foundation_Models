'''

'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, k, a):
    for i in range(n):
        if a[i]%k==0:
            a[i]=a[i]//k
        else:
            a[i]=a[i]//k+1
    if sum(a)==n-1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = solve(n, k, a)

        fptr.write(result + '\n')

    fptr.close()