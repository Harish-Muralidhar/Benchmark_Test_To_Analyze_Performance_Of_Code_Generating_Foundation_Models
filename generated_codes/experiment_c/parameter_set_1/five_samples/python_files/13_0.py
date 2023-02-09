"""


"""

import math

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def isConnected(p1,p2,r):
    return distance(p1,p2) <= r

for _ in range(int(input())):
    r = int(input())
    p = []
    p.append(tuple(int(i) for i in input().split()))
    p.append(tuple(int(i) for i in input().split()))
    p.append(tuple(int(i) for i in input().split()))
    if isConnected(p[0],p[1],r) and isConnected(p[1],p[2],r) and isConnected(p[2],p[0],r):
        print("yes")
    else:
        print("no")