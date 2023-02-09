"""

Explanation

In the first case, all three can communicate directly. In the second case, the Chef and the head server are close enough to communicate directly. The sous-chef can communicate with the other two by going through the Chef. In the third case, any two can communicate, but all three cannot.

"""
import math

def is_triplet_connected(r,x1,y1,x2,y2,x3,y3):
    d12 = math.hypot(x1 - x2, y1 - y2)
    d13 = math.hypot(x1 - x3, y1 - y3)
    d23 = math.hypot(x2 - x3, y2 - y3)
    if d12 <= r and d13 <= r and d23 <= r:
        return True
    elif d12 <= r and d13 <= r:
        return True
    elif d12 <= r and d23 <= r:
        return True
    elif d23 <= r and d13 <= r:
        return True
    else:
        return False
    
    
    
n = int(input())
for _ in range(n):
    r = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())
    print("yes" if is_triplet_connected(r,x1,y1,x2,y2,x3,y3) else "no")