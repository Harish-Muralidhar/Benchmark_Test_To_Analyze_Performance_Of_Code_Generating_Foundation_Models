'''


'''

import sys

def lights(n):
    if n==1:
        return 2
    else:
        return (n*2) + (n-1)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(lights(n))