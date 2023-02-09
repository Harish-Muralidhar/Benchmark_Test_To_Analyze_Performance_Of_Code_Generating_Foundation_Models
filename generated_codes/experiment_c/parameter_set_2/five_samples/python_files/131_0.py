'''

'''

import math

def get_money(M, p):
    if p == 1:
        return 1000000000, 0
    else:
        return 1000000000 * p**M, 1000000000 * (1 - p**M)

def main():
    T = int(input())
    for _ in range(T):
        M, p = map(float, input().split())
        print(*get_money(M, p))

if __name__ == '__main__':
    main()