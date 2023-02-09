'''


'''

import math

def max_coins(n,k):
    if n%k == 0:
        return int(n/k)
    else:
        return int(n/k) + 1

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        n,k = map(int,input().split())
        print(max_coins(n,k))