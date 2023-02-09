"""

"""

#Solution:
import math
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    l = [list(input()) for i in range(R)]
    count = 0
    for i in range(R):
        for j in range(C):
            if l[i][j] == '^':
                L, R, T, B = 0, 0, 0, 0
                x, y = i, j
                while x>=0 and l[x][j] == '^':
                    T += 1
                    x -= 1
                x, y = i, j
                while x<R and l[x][j] == '^':
                    B += 1
                    x += 1
                x, y = i, j
                while y>=0 and l[i][y] == '^':
                    L += 1
                    y -= 1
                x, y = i, j
                while y<C and l[i][y] == '^':
                    R += 1
                    y += 1
                if math.gcd(math.gcd(L, R), math.gcd(T, B)) > 1:
                    count += 1
    print(count)

"""
t=int(input())
for i in range(t):
    r,c=map(int,input().split())
    l=[]
    for j in range(r):
        l.append(input())
    count=0
    for j in range(r):
        for k in range(c):
            if l[j][k]=='^':
                l1=l2=t1=t2=0
                for p in range(j):
                    if l[p][k]=='^':
                        t1+=1
                    else:
                        break
                for p in range(j+1,r):
                    if l[p][k]=='^':
                        t2+=1
                    else:
                        break
                for p in range(k):
                    if l[j][p]=='^':
                        l1+=1
                    else:
                        break
                for p in range(k+1,c):
                    if l[j][p]=='^':
                        l2+=1
                    else:
                        break
                if math.gcd(math.gcd(l1,l2),math.gcd(t1,t2))>1:
                    count+=1
    print(count)
"""