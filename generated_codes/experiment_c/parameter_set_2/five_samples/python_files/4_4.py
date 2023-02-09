'''


'''

import math
import os
import random
import re
import sys

# Complete the chefAndSubarrays function below.
def chefAndSubarrays(a):
    count=0
    for i in range(len(a)):
        sum=0
        product=1
        for j in range(i,len(a)):
            sum+=a[j]
            product*=a[j]
            if sum==product:
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = chefAndSubarrays(a)

        fptr.write(str(result) + '\n')

    fptr.close()