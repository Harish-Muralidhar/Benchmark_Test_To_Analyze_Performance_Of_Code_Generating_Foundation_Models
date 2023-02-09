'''

'''

import math

def perimeter(x, y, r):
    return 2 * math.pi * r

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def circle_intersection(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    if d > (r1 + r2):
        return 0
    elif d < abs(r1 - r2):
        return min(r1, r2) * math.pi
    else:
        a = (r1**2 - r2**2 + d**2) / (2*d)
        h = math.sqrt(r1**2 - a**2)
        theta1 = 2 * math.acos(a/r1)
        theta2 = 2 * math.acos((d - a)/r2)
        area1 = 0.5 * theta1 * r1**2 - 0.5 * r1**2 * math.sin(theta1)
        area2 = 0.5 * theta2 * r2**2 - 0.5 * r2**2 * math.sin(theta2)
        return area1 + area2

def main():
    T = int(input())
    for t in range(T):
        W, H, N = map(int, input().split())
        circles = []
        for i in range(N):
            x, y, r = map(float, input().split())
            circles.append((x, y, r))
        circles.sort(key=lambda x: x[2], reverse=True)
        total_perimeter = 0
        for i in range(N):
            x1, y1, r1 = circles[i]
            perimeter_i = perimeter(x1, y1, r1)
            for j in range(i+1, N):
                x2, y2, r2 = circles[j]