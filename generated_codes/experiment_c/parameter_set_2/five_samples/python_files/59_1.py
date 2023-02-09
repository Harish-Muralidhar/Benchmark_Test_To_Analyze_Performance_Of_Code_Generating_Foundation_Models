'''

'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr):
    n = len(arr)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            if arr[i-1] >= arr[j]:
                dp[i] += dp[j]
                dp[i] = dp[i]%1000000009
    return dp[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = solve(arr)

        fptr.write(str(result) + '\n')

    fptr.close()