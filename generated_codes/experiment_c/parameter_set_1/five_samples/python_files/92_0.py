'''

'''

import math
import os
import random
import re
import sys

def candies(n, arr, k):
    if k == 1:
        return sum(arr)
    else:
        arr.sort()
        for i in range(n):
            if sum(arr[i:i+k]) % k == 0:
                return sum(arr[i:i+k])
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        k = int(nm[2])
        arr = list(map(int, input().rstrip().split()))
        result = candies(n, arr, k)
        fptr.write(str(result) + '\n')
    fptr.close()