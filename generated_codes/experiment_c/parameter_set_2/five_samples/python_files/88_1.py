"""


Note

In the first sample test the grid is too small to show the real power of Loda.



"""



# Write your code here

import sys

def main():
    n,m,q=map(int,sys.stdin.readline().split())
    sx,sy=map(int,sys.stdin.readline().split())
    p1=[0]*6
    p2=[0]*6
    for i in range(6):
        p1[i],p2[i]=map(int,sys.stdin.readline().split())
    t=[]
    for i in range(q):
        t.append(int(sys.stdin.readline()))
    for i in range(q):
        print(calculate(n,m,sx,sy,p1,p2,t[i]))

def calculate(n,m,sx,sy,p1,p2,t):
    c=1
    for i in range(t):
        c+=get_images(n,m,sx,sy,p1,p2)
    return c

def get_images(n,m,sx,sy,p1,p2):
    c=0
    for i in range(n):
        for j in range(m):
            if i==sx-1 and j==sy-1:
                c+=1
            elif i==sx-1 and j%p2[1]==sy-1:
                c+=1
            elif j==sy-1 and i%p1[0]==sx-1:
                c+=1
            elif i==sx-1 and j%p2[2]==sy-1 and i%p1[2]==sx-1:
                c+=1
            elif j==sy-1 and i%p1[3]==sx-1 and j%p2[3]==sy-1:
                c+=1
            elif i==sx-1 and j%p2[4]==sy-1 and j%