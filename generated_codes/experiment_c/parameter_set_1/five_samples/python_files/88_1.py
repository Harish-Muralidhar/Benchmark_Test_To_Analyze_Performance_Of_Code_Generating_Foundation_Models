"""


"""
# cook your dish here
"""
# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and a[i][j]>0:
                a[i][j] = 1
            if i>0 and a[i][j]>0:
                a[i][j] = a[i-1][j] + a[i][j]
    s = 0
    for i in range(n):
        for j in range(m):
            if a[i][j]>0:
                s += a[i][j]
    print(s)
"""
"""
P = [list(map(int,input().split())) for i in range(6)]
for _ in range(int(input())):
    T = int(input())
    s = 0
    for i in range(6):
        for j in range(6):
            if P[i][j]>0:
                s+=P[i][j]
    print(s)
"""

N, M, Q = map(int, input().split())
Sx, Sy = map(int, input().split())
P = [list(map(int, input().split())) for i in range(6)]
for _ in range(Q):
    T = int(input())
    s = 0
    for i in range(6):
        for j in range(6):
            if P[i][j] > 0:
                s += P[i][j]
    print(s)