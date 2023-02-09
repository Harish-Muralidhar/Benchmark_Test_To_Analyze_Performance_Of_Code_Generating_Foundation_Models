'''


'''

import math

def xor_sum(n):
    if n%4 == 0:
        return n
    elif n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    else:
        return 0

def find_num_seq(n, a):
    x = 0
    for i in range(n):
        x ^= a[i]
    return xor_sum(x)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(find_num_seq(n, a))

if __name__ == '__main__':
    main()