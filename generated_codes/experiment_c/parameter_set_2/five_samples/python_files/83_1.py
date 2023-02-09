"""

"""

import sys
import os
import math

def minPartialSum(n,k,p,arr):
    minSum = sys.maxsize
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum >= k and sum%p < minSum:
                minSum = sum%p
    return minSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkp = input().split()

    n = int(nkp[0])

    k = int(nkp[1])

    p = int(nkp[2])

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = minPartialSum(n,k,p,arr)

    fptr.write(str(result) + '\n')

    fptr.close()