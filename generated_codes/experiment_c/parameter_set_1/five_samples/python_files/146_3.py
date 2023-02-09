'''


'''

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    passes = 0
    value = 0
    while n > value:
        if (p > n) and (value < n):
            required = math.ceil((n - value) / (m * w))
            passes += required
            value += m * w * required
        else:
            if (m * w) < n:
                temp = math.floor((p / (m * w)))
                if temp == 0:
                    temp = 1
                value = value + temp * (m * w)
                passes += temp
                if (p - temp * (m * w)) > n - value:
                    return passes
            else:
                if (m * w) == n:
                    return passes + 1
                else:
                    return n
        if p > n - value:
            p = n - value
        if (m * w) < n - (value + p):
            m += 1
        else:
            w += 1
    return passes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()