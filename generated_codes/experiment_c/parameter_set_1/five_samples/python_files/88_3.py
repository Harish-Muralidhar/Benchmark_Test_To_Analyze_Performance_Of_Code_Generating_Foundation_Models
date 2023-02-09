'''


'''

import math

N,M,Q = map(int,input().split())
Sx,Sy = map(int,input().split())

P1 = [int(x) for x in input().split()]
P2 = [int(x) for x in input().split()]


for i in range(Q):
    T = int(input())
    count = 1
    for i in range(1,T+1):
        x = Sx + P1[(i-1)%6] * i
        y = Sy + P2[(i-1)%6] * i
        if x >= 1 and x <= N and y >= 1 and y <= M:
            count += 1
    print(count)