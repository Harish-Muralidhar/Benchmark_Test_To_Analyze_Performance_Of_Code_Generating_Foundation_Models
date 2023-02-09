'''

'''

import math

def minimum_operations(a, b):
    count = 0
    while a !=b:
        if a % 2 == 0:
            if a > b:
                a = a / 2
                count += 1
            else:
                b = b / 2
                count += 1
        else:
            if a > b:
                a = (a - 1) / 2
                count += 1
            else:
                b = (b - 1) / 2
                count += 1
    return count


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(minimum_operations(a, b))