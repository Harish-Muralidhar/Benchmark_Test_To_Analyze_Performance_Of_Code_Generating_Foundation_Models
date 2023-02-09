'''
'''

import math

def menu_count(p):
    count = 0
    while p > 0:
        count += p % 2
        p = p // 2
    return count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        p = int(input())
        print(menu_count(p))