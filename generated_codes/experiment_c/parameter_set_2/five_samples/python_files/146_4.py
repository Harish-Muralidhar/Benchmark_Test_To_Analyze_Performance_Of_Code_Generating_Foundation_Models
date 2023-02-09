'''


'''

import math
import os
import random
import re
import sys

# Complete the minimumTime function below.
def minimumTime(numOfSubFiles, files):
    # Return the minimum time needed to process all the subfiles.
    # Write your code here
    files.sort()
    print(files)
    min_time = 0
    while len(files) > 1:
        min_time += files[0]
        for i in range(len(files)):
            if files[i] == files[0]:
                files[i] = files[i]//2
            else:
                files[i] -= files[0]
        files = [x for x in files if x > 0]
        files.sort()
        print(files)
    min_time += files[0]
    return min_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numOfSubFiles = int(input())

    files = list(map(int, input().rstrip().split()))

    result = minimumTime(numOfSubFiles, files)

    fptr.write(str(result) + '\n')

    fptr.close()