'''


'''



import math
import os
import random
import re
import sys

# Complete the function below.

def canTransform(N):
    for i in range(int(N/2),N+1):
        if (i**2+((i*2)**2)==(N**2)):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        N = int(input())

        result = canTransform(N)

        fptr.write(result + '\n')

    fptr.close()

'''
import math
import os
import random
import re
import sys

# Complete the function below.

def canTransform(N):
    if N%2==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        N = int(input())

        result = canTransform(N)

        fptr.write(result + '\n')

    fptr.close()
'''