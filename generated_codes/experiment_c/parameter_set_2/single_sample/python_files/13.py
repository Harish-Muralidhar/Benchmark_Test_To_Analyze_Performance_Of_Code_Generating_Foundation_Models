'''


'''

import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def can_communicate(x1,y1,x2,y2,x3,y3,r):
    if distance(x1,y1,x2,y2) <= r:
        return True
    elif distance(x1,y1,x3,y3) <= r:
        return True
    elif distance(x2,y2,x3,y3) <= r:
        return True
    else:
        return False

def main():
    t = int(input())
    for _ in range(t):
        r = int(input())
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        x3,y3 = map(int,input().split())
        if can_communicate(x1,y1,x2,y2,x3,y3,r):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    main()