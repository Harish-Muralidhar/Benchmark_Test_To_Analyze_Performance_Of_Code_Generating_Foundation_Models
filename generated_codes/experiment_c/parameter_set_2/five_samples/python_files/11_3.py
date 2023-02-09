'''

'''

import math

def menu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 + menu(n - int(math.log(n,2)))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(menu(n))