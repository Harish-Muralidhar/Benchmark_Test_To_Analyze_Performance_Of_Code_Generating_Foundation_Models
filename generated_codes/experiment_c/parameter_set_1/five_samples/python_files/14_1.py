'''

Solution:
'''

import math

def minimumOperations(initialVal, finalVal):
    count = 0
    while(initialVal < finalVal):
        if(finalVal%2 == 0):
            finalVal = finalVal / 2
            count += 1
        else:
            finalVal = (finalVal - 1) / 2
            count += 2
    return count

t = int(input())
for _ in range(t):
    initialVal, finalVal = map(int, input().split())
    print(minimumOperations(initialVal, finalVal))