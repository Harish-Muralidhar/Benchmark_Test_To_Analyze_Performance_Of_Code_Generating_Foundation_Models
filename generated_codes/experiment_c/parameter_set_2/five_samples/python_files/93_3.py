'''

'''

import math

def sum_of_kth_powers(n, k, p):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i, k)
    return sum % p

def main():
    t = int(input())
    for i in range(t):
        n, k, p = map(int, input().split())
        print(sum_of_kth_powers(n, k, p))

if __name__ == '__main__':
    main()