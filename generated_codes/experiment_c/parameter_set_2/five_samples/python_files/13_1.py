"""

Explanation

In the first case, all three are already close enough to communicate directly.

In the second case, the Chef and the head server are close enough to communicate directly, but the sous-chef is too far away from the head server. However, the sous-chef and the Chef are close enough to the head server so they can still communicate with each other using the head server as an intermediate transceiver.

In the third case, any two are close enough to communicate directly, but the Chef and the sous-chef are too far apart to communicate through the head server.

"""

import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def is_possible(R,x1,y1,x2,y2,x3,y3):
    if distance(x1,y1,x2,y2) <= R:
        return True
    elif distance(x1,y1,x3,y3) <= R:
        return True
    elif distance(x2,y2,x3,y3) <= R:
        return True
    elif distance(x1,y1,x2,y2) <= R + distance(x1,y1,x3,y3):
        return True
    elif distance(x1,y1,x3,y3) <= R + distance(x1,y1,x2,y2):
        return True
    elif distance(x2,y2,x3,y3) <= R + distance(x1,y1,x2,y2):
        return True
    else:
        return False

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        R = int(input())
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        x3,y3 = map(int,input().split())
        if is_possible