'''


'''

import math

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
 
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area (x1, y1, x2, y2, x3, y3)
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    return (A == A1 + A2 + A3)

def isInsideCircle(x1, y1, x2, y2, r):
    return ((x1-x2)**2 + (y1-y2)**2) <= r**2

def isIntersect(x1, y1, r1, x2, y2, r2):
    return ((x1-x2)**2 + (y1-y2)**2) <= (r1+r2)**2

def isIntersectCircleRect(x1, y1, r1, x2, y2, x3, y3):
    return isInsideCircle(x1, y1, x2, y2, r1) or isInsideCircle(x1, y1, x3, y3, r1) or isInsideCircle(x1, y1, x2, y3, r1) or isInsideCircle(x1, y1, x3, y2, r1)

def isIntersectCircleCircle(x1, y1, r1, x2, y2, r2):
    return isIntersect(x1, y1, r1, x2, y2, r2) and not isInsideCircle(x1, y1