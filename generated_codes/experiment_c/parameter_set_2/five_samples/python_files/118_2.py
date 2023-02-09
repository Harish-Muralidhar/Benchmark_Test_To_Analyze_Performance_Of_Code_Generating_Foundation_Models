'''

'''

import math
import os
import random
import re
import sys

# Complete the function below.

def  getMinimumCost(n, k, c):
    c.sort()
    c = c[::-1]
    ans = 0
    for i in range(n):
        ans += (1+i//k)*c[i]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(n, k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()