'''

'''

#import 
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    
    swap=0
    for i in range(len(q)):
        if(q[i]-i-1)>2:
            print('Too chaotic')
            return
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                swap+=1
    print(swap)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)