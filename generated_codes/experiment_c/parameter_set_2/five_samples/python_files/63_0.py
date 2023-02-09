'''


'''

import math

def is_inside(x, y, r, x1, y1):
    return math.sqrt((x-x1)**2 + (y-y1)**2) <= r

def get_intersection(x, y, r, x1, y1, r1):
    d = math.sqrt((x-x1)**2 + (y-y1)**2)
    if d > r + r1:
        return 0, 0, 0, 0
    if d < abs(r - r1):
        return 0, 0, 0, 0
    if d == 0 and r == r1:
        return 0, 0, 0, 0
    a = (r**2 - r1**2 + d**2) / (2*d)
    h = math.sqrt(r**2 - a**2)
    x2 = x + a*(x1 - x)/d
    y2 = y + a*(y1 - y)/d
    x3 = x2 + h*(y1 - y)/d
    y3 = y2 - h*(x1 - x)/d
    x4 = x2 - h*(y1 - y)/d
    y4 = y2 + h*(x1 - x)/d
    return x3, y3, x4, y4

def get_angle(x, y, x1, y1):
    return math.atan2(y1-y, x1-x)

def get_perimeter(x, y, r, x1, y1, r1):
    x3, y3, x4, y4 = get_intersection(x, y, r, x1, y1, r1)
    if x3 == 0 and y3 == 0 and x4 == 0 and y4 == 0:
        return 0
    angle1 = get_angle(x, y, x3, y3)
    angle2 = get_angle(x, y, x4, y4)
    if angle1 > angle2:
        angle1, angle2 = angle2, angle