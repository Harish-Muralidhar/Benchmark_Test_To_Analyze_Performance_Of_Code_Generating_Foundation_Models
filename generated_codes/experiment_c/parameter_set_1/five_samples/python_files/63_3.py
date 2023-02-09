



import math
import numpy as np

def get_distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def get_perimeter(x1,y1,x2,y2,r):
    return 2*math.acos(1-(get_distance(x1,y1,x2,y2)**2)/(2*r**2))*r


def get_center_points(x1,y1,r1,x2,y2,r2):
    m = (y2-y1)/(x2-x1)
    c = y1-m*x1
    a = 1 + m**2
    b = 2*(m*c-m*y1-x1)
    d = (c**2)+(x1**2)-(2*c*y1)+(y1**2)-(r1**2)

    x3 = (-b + math.sqrt((b**2)-(4*a*d)))/(2*a)
    y3 = m*x3+c

    x4 = (-b - math.sqrt((b**2)-(4*a*d)))/(2*a)
    y4 = m*x4+c

    return [[x3,y3][x4,y4]]



def perimeter(w,h,n,circles):
    perimeter = 0

    for i in range(n-1):
        for j in range(i+1,n):
            x1,y1,r1 = circles[i][0],circles[i][1],circles[i][2]
            x2,y2,r2 = circles[j][0],circles[j][1],circles[j][2]

            if (x1==x2 and y1==y2 and r1==r2):
                continue

            if (( x1 < x2 and r1 < r2 ) or ( x1 > x2 and r1 > r2)):
                x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

            if (x1==x2 and y1==y2 and r1!=r2):
                perimeter += 0

            if (x1==x2 and y1!=y2 and r1!=r2):
                if (max(y1,y2)-min(y1,y2) <= max(r1,r2)):
                    perimeter += 0
                else:
                    perimeter += 2*abs(r1-r2)

            else:
                centers = get_center_points(x1,y1,r1,x2,y2,r2)

                for c in centers:
                    if ( (c[0]>=0 and c[0]<=w) and (c[1]>=0 and c[1]<=h) ):
                        perimeter += 2*get_perimeter(x1,y1,c[0],c[1],r1)
                    else:
                        perimeter += 2*math.acos(1-(get_distance(x1,y1,x2,y2)**2)/(2*r1**2))*r1

    return perimeter



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        w,h,n = [int(x) for x in input().split()]
        circles = []
        for i in range(n):
            x,y,r = [float(x) for x in input().split()]
            circles.append([x,y,r])

        print(perimeter(w,h,n,circles))