'''


'''

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + " " + str(self.y)
    def __repr__(self):
        return str(self.x) + " " + str(self.y)

def int_in_circle(circle, p):
    r = circle[2]
    return (circle[0]-p.x)**2+(circle[1]-p.y)**2 <= r**2

def int_circle_circle(c1, c2):
    r1 = c1[2]
    r2 = c2[2]
    return (c1[0]-c2[0])**2+(c1[1]-c2[1])**2 <= (r1+r2)**2

def circle_line_intersection(circle, line):
    """
    Finds points of intersection between a circle and a line.
    """
    slope = (line.p2.y - line.p1.y) / (line.p2.x - line.p1.x)
    y_intercept = line.p1.y - slope*line.p1.x
    center = Point(circle[0],circle[1])
    radius = circle[2]
    a = 1.0 + slope**2
    b = -2.0*center.x + 2.0*slope*(y_intercept - center.y)
    c = (y_intercept - center.y)**2 - radius**2 + center.x**2

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -0.5*b/a
        y = slope*x + y_intercept
        return [Point(x,y)]
    else:
        x1 = (-0.5*b + math.sqrt(discriminant))/a
        y1 = slope*x1 + y_intercept
        x2 = (-0.5*b - math.sqrt(discriminant))/a
        y2 = slope*x2 + y_intercept
        return [Point(x1,y1), Point(x2,y2)]

def in_range(x1, x2, x):
    if x1 > x2:
        return x > x2 and x < x1
    else:
        return x > x1 and x < x2

def in_triangle(pt, p1, p2, p3):
    b1 = sign(pt, p1, p2) < 0.0
    b2 = sign(pt, p2, p3) < 0.0
    b3 = sign(pt, p3, p1) < 0.0
    return ((b1 == b2) and (b2 == b3))

def sign(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

def area_triangle(p1, p2, p3):
    return abs((p1.x*(p2.y-p3.y) + p2.x*(p3.y-p1.y)+ p3.x*(p1.y-p2.y))/2.0)

def in_circle(p, center, radius):
    return (p.x-center.x)**2 + (p.y-center.y)**2 <= radius**2

def area_circle(radius):
    return math.pi*radius**2

def area_sector(radius, theta):
    return 0.5*radius**2*(theta-math.sin(theta))

def area_triangle_circle(c, r, a, b, theta):
    p = area_triangle(a, b, c)
    t = area_sector(r, theta)
    return p-t

def perimeter(c, r, a, b, theta):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta

def perimeter_triangle_circle(c, r, a, b, theta):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta

def perimeter_circle_circle(c1, r1, c2, r2, theta1, theta2):
    return (c1.x-c2.x)**2+(c1.y-c2.y)**2+\
           r1*theta1+r2*theta2

def perimeter_circle_sector(c, r, a, b, theta):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta

def perimeter_triangle_segment(c, r, a, b, theta):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta

def perimeter_triangle_segments(c, r, a, b, theta1, theta2):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta1+r*theta2

def perimeter_triangle_segment_segment(c, r, a, b, theta1, theta2):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta1+r*theta2

def perimeter_triangle_segment_segment_segment(c, r, a, b, theta1, theta2, theta3):
    return (c.x-a.x)**2+(c.y-a.y)**2+\
           (c.x-b.x)**2+(c.y-b.y)**2+\
           r*theta1+r*theta2+r*theta3

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def intersect_line_segment(line, seg):
    x1,y1 = line.p1.x,line.p1.y
    x2,y2 = line.p2.x,line.p2.y
    x3,y3 = seg.p1.x,seg.p1.y
    x4,y4 = seg.p2.x,seg.p2.y

    def ccw(A,B,C):
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

    # Return true if line segments AB and CD intersect
    return ccw(line.p1,seg.p1,seg.p2) != ccw(line.p2,seg.p1,seg.p2) and ccw(line.p1,line.p2,seg.p1) != ccw(line.p1,line.p2,seg.p2)

def angle(a, o, b):
    aob = math.acos(((a.x-o.x)*(b.x-o.x)+(a.y-o.y)*(b.y-o.y))/(r[i]*r[j]))
    if aob > math.pi:
        aob = 2*math.pi - aob
    return aob

def small_angle(a, o, b):
    aob = math.acos(((a.x-o.x)*(b.x-o.x)+(a.y-o.y)*(b.y-o.y))/(r[i]*r[j]))
    return aob

def norm(vec):
    return math.sqrt(vec.x**2+vec.y**2)

def dot(v1, v2):
    return v1.x*v2.x+v1.y*v2.y

def cross(v1, v2):
    return v1.x*v2.y-v1.y*v2.x

def area_triangle_given_three_sides(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def perimeter_triangle_given_three_sides(a, b, c):
    return a+b+c

def area_triangle_given_two_sides_and_angle_between(a, b, theta):
    return 0.5*a*b*math.sin(theta)

def area_triangle_given_two_angles_and_side_between(a, b, A):
    return 0.5*a*b*math.sin(A)

def area_triangle_given_two_sides_and_angle_opposite_of(a, b, c):
    return 0.5*b*c*math.sin(a)

def perimeter_triangle_given_side_and_two_angles(a, b, c):
    return a+b+c

def area_regular_polygon(n, s):
    return 0.25*n*s**2*cot(math.pi/n)

def area_ellipse(a, b):
    return math.pi*a*b

def area_segment(r, theta):
    return r**2*(theta-math.sin(theta))/2

def area_sector(r, theta):
    return 0.5*r**2*theta

def area_trapezoid(a, b, h):
    return 0.5*(a+b)*h

def area_trap(r1, r2, h):
    return h*(r1+r2)/2

def area_parallelogram(b, h):
    return b*h

def area_kite(d1, d2):
    return 0.5*d1*d2

def area_rhombus(d1, d2):
    return 0.5*d1*d2

def area_circle_given_arc_and_chord(a, c):
    return 0.5*a*c

def area_circle_given_arc_and_tangent(a, t):
    return 0.5*a*t

def area_circle_given_radius_and_tangent(r, t):
    return 0.5*r*t

def area_circle_given_radius_and_chord(r, c):
    return 0.5*r*c

def area_circle_given_radius_and_angle(r, theta):
    return 0.5*r*r*theta

def area_circle_given_diameter_and_angle(d, theta):
    return 0.25*d*d*theta

def area_circle_given_diameter_and_chord(d, c):
    return d*c*(1-math.cos(c/d))/(4*math.sin(c/d))

def area_circle_given_diameter_and_tangent(d, t):
    return d*t*(1-math.cos(t/d))/(4*math.sin(t/d))

def area_circle_given_tangent_and_chord(t, c):
    return t*c*(1-math.cos(c/t))/(4*math.sin(c/t))

def area_circle_given_two_tangents(r, t1, t2):
    return r*r*math.acos((r-t1)*(r-t2)/(r*r))-\
           0.5*math.sqrt((-r+t1+t2)*(r+t1-t2)*(r-t1+t2)*(r+t1+t2))

def area_circle_given_tangent_and_radius(r, t):
    return 0.25*(4*r*r-(t*t))*math.asin(t/(2*r))

def area_circle_given_tangent_and_angle(a, t):
    return 0.25*(a-t)*t*(4*a*a-(t*t))/a

def area_circle_given_tangent_and_side(t, s):
    return (t*s)/2

def area_circle_given_chord_and_radius(r, c):
    return r*r*math.acos((r-c)/r)-\
           0.5*math.sqrt((-r+c)*(r+c)*(r+c-2*c*r))

def area_circle_given_chord_and_angle(a, c):
    return 0.5*(a-c)*c

def area_circle_given_chord_and_side(c, s):
    return c*s*(1-math.cos(c/s))/(2*math.sin(c/s))

def area_circle_given_chord_and_tangent(c, t):
    return 0.5*c*t

def area_circle_given_two_radii(r1, r2):
    return math.pi*r1*r2

def area_circle_given_two_chords(c1, c2):
    return 0.5*(c1*c2)*(1-math.cos(c1/c2))/(2*math.sin(c1/c2))

def area_circle_given_two_tangents(t1, t2):
    return 0.25*math.sqrt((4*t1*t1*t2*t2)-(t1*t1+t2*t2-2*t1*t2)**2)

def perimeter_circle_given_diameter(d):
    return math.pi*d

def perimeter_circle_given_radius(r):
    return 2*math.pi*r

def perimeter_circle_given_arc_and_chord(a, c):
    return c+2*math.sqrt(a*c-0.25*c*c)

def perimeter_circle_given_arc_and_tangent(a, t):
    return t+2*math.sqrt(a*t-0.25*t*t)

def perimeter_circle_given_radius_and_tangent(r, t):
    return t+2*math.sqrt(r*r-0.25*t*t)

def perimeter_circle_given_radius_and_chord(r, c):
    return c+2*math.sqrt(r*r-0.25*c*c)

def perimeter_circle_given_radius_and_angle(r, theta):
    return 2*r*math.sin(theta/2)

def perimeter_circle_given_diameter_and_angle(d, theta):
    return d*math.sin(theta/2)

def perimeter_circle_given_diameter_and_chord(d, c):
    return c+2*math.sqrt(d*d*(1-math.