"""


"""

import math

def check_intersection(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d > r1+r2:
        return 0
    elif d < abs(r1-r2):
        return 0
    else:
        return 1

def find_angle(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = math.sqrt(r1**2 - a**2)
    x3 = x1 + a*(x2-x1)/d
    y3 = y1 + a*(y2-y1)/d
    x4 = x3 + h*(y2-y1)/d
    y4 = y3 - h*(x2-x1)/d
    x5 = x3 - h*(y2-y1)/d
    y5 = y3 + h*(x2-x1)/d
    return (x4,y4,x5,y5)

def find_angle_1(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = math.sqrt(r1**2 - a**2)
    x3 = x1 + a*(x2-x1)/d
    y3 = y1 + a*(y2-y1)/d
    x4 = x3 + h*(y2-y1)/d
    y4 = y3 - h*(x2-x1)/d
    x5 = x3 -