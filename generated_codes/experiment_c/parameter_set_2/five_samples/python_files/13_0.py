"""

Explanation

In the first case, all three are already close enough to communicate directly.

In the second case, the Chef and the head server are close enough to communicate directly, but the Chef and the sous-chef must communicate through the head server because they are too far apart.

In the third case, no two are close enough to communicate directly, and it is not possible for all three to communicate through one other transceiver.

"""

import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def chef_communication(r,x1,y1,x2,y2,x3,y3):
    if distance(x1,y1,x2,y2) <= r:
        if distance(x1,y1,x3,y3) <= r or distance(x2,y2,x3,y3) <= r:
            return "yes"
        else:
            return "no"
    elif distance(x1,y1,x3,y3) <= r:
        if distance(x2,y2,x3,y3) <= r:
            return "yes"
        else:
            return "no"
    elif distance(x2,y2,x3,y3) <= r:
        if distance(x1,y1,x3,y3) <= r:
            return "yes"
        else:
            return "no"
    else:
        return "no"

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        r = int(input())
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        x3,y3 = map(int,input().split())
        print(chef_communication(r,x1,y1,x2,y2,x3,y3))