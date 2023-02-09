"""
"""

import sys
sys.stdin = open("input.txt",'r')
sys.stdout = open("output.txt",'w')

def cops(m,x,y,h):
    lst = []
    for i in range(m):
        n = h[i]
        while(n>0 and n<101):
            lst.append(n)
            n -= 1
        n = h[i]
        while(n>0 and n<101):
            lst.append(n)
            n += 1
        lst.sort()
        cop = 0
        for i in range(1,101):
            if i in lst:
                cop += 1
        print(100-cop)

for _ in range(int(input())):
    m,x,y = map(int,input().split())
    h = list(map(int,input().split()))
    cops(m,x,y,h)