'''


'''

import math

def get_min_operations(a,b):
    count = 0
    while a != b:
        if a > b:
            a = a // 2
            count += 1
        else:
            a = a * 2
            count += 1
    return count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()][0:2]
        print(get_min_operations(a,b))