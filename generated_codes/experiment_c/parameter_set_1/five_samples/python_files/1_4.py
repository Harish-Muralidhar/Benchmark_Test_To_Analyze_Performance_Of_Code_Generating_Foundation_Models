'''

'''

#!/bin/python3

import os
import sys

#
# Complete the alternatingSubarray function below.
#
def alternatingSubarray(a):
    #
    # Write your code here.
    #
    n = len(a)
    dp = [1]*n
    flag = [0]*n
    if a[0] < 0:
        flag[0] = 1
    for i in range(1,n):
        if a[i] < 0 and flag[i-1] == 0:
            flag[i] = 1
            dp[i] = dp[i-1] + 1
        elif a[i] > 0 and flag[i-1] == 1:
            flag[i] = 0
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    return dp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = alternatingSubarray(a)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()