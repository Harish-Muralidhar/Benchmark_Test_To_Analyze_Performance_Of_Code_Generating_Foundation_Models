'''


'''

import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_intersection_points(x1, y1, r1, x2, y2, r2):
    d = get_distance(x1, y1, x2, y2)
    if d > r1 + r2:
        return None
    if d < abs(r1 - r2):
        return None
    if d == 0 and r1 == r2:
        return None

    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    xm = x1 + a * (x2 - x1) / d
    ym = y1 + a * (y2 - y1) / d
    xs1 = xm + h * (y2 - y1) / d
    xs2 = xm - h * (y2 - y1) / d
    ys1 = ym - h * (x2 - x1) / d
    ys2 = ym + h * (x2 - x1) / d

    return [(xs1, ys1), (xs2, ys2)]

def get_intersection_area(x1, y1, r1, x2, y2, r2):
    d = get_distance(x1, y1, x2, y2)
    if d > r1 + r2:
        return 0
    if d < abs(r1 - r2):
        return 0
    if d == 0 and r1 == r2:
        return 0

    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    xm = x1 + a * (x2 - x1) / d
    ym = y1 + a *