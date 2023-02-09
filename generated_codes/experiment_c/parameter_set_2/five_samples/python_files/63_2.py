'''

'''

import math
import sys

def get_perimeter(x,y,r):
    return 2*math.pi*r

def get_intersection_points(x1,y1,r1,x2,y2,r2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d > r1+r2:
        return None
    if d < abs(r1-r2):
        return None
    if d == 0 and r1 == r2:
        return None
    a = (r1**2 - r2**2 + d**2) / (2*d)
    h = math.sqrt(r1**2 - a**2)
    xm = x1 + a*(x2-x1)/d
    ym = y1 + a*(y2-y1)/d
    xs1 = xm + h*(y2-y1)/d
    xs2 = xm - h*(y2-y1)/d
    ys1 = ym - h*(x2-x1)/d
    ys2 = ym + h*(x2-x1)/d
    return (xs1,ys1),(xs2,ys2)

def get_angle(x,y,x1,y1):
    return math.atan2(y1-y,x1-x)

def get_angle_diff(a1,a2):
    return (a2-a1+math.pi)%(2*math.pi)-math.pi

def get_arc_length(x,y,r,a1,a2):
    return r*abs(get_angle_diff(a1,a2))

def get_segment_length(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_segment_intersection(x1,y1,x2,y2,x3