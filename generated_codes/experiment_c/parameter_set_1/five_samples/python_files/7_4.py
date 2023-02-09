'''

In the third example,
you will need to paint 2 balloons. So the answer is 2.
'''

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s):
    total = len(s)
    count1 = s.count('a')
    count2 = s.count('b')
    if count1>count2:
        return count2
    else:
        return count1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    result = birthday(s)

    fptr.write(str(result) + '\n')

    fptr.close()