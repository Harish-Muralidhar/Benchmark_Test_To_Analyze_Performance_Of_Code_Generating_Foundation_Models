'''

Explanation

In the first case, all three people are already close enough to communicate directly without an intermediate transceiver.

In the second case, the Chef and the head server are close enough to communicate directly, but the sous-chef is too far away from the Chef and the head server. However, the sous-chef is close enough to the head server so they can still communicate with each other using the head server as an intermediate transceiver.

In the third case, no two people are close enough to communicate directly, and there are no three people such that each pair is close enough to communicate directly.

'''

import math

def is_close(x1,y1,x2,y2,r):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d <= r:
        return True
    return False

def is_possible(x1,y1,x2,y2,x3,y3,r):
    if is_close(x1,y1,x2,y2,r) or is_close(x1,y1,x3,y3,r) or is_close(x2,y2,x3,y3,r):
        return True
    return False

t = int(input())
for i in range(t):
    r = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    if is_possible(x1,y1,x2,y2,x3,y3,r):
        print("yes")
    else:
        print("no")