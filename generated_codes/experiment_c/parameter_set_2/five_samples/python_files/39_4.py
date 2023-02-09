"""


"""

import math

def max_coins(n,k):
    if n < k:
        return n
    else:
        return math.floor(n/k)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,k = map(int,input().split())
        print(max_coins(n,k))