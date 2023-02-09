'''
'''

import math

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

for i in range(int(input())):
    k = int(input())
    print(truncate(103993/33102, k))