'''

Solution

'''

import math

def countPairs(n, u, v):
    u1 = math.floor(math.log2(u))
    v1 = math.floor(math.log2(v))
    u2 = math.floor(math.log2(u))
    if u1 == v1:
        return n // 2 + 1
    elif u2 == 1:
        return n // 2
    else:
        return n

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n, u, v = map(int, input().split())
        print(countPairs(n, u, v))