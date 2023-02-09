'''

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the examRush function below.
def examRush(tm, t):
    
    tm = tm.sort()
    tm = [0] + tm
    r = len(tm) - 1
    ans = 0

    for i in range(len(t)-1,-1,-1):
        tm[i] += tm[i+1]
    
    for i in range(len(t)):
        if tm[i] + t[i] >= tm[-1] - tm[i]:
            ans = max(ans, t[i])
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    t = list(map(int, input().rstrip().split()))

    tm = list(map(int, input().rstrip().split()))

    result = examRush(tm, t)

    fptr.write(str(result) + '\n')

    fptr.close()