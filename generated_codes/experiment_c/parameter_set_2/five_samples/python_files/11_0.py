'''

'''

import math

def min_menu_count(p):
    menu_count = 0
    for i in range(12, -1, -1):
        if p >= 2**i:
            menu_count += p // 2**i
            p = p % 2**i
    return menu_count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        p = int(input())
        print(min_menu_count(p))