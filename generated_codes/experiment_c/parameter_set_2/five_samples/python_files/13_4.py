"""

Explanation

In the first case, all three are already close enough to communicate directly. In the second case, the Chef and the head server are close enough to communicate directly, but the sous-chef must communicate with the Chef through the head server. In the third case, no two are close enough to communicate directly, so it is not possible for all three to communicate.

"""

import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        R = int(input())
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        x3,y3 = map(int,input().split())
        if distance(x1,y1,x2,y2) <= R or distance(x1,y1,x3,y3) <= R or distance(x2,y2,x3,y3) <= R:
            print("yes")
        else:
            print("no")