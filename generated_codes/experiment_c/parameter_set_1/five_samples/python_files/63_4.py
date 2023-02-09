"""


"""
#Solution
import math
#Function to calculate distance between two points


def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

#Function to calculate area of the polygon formed by given vertices
def area(x,y,n):
    ans = 0
    for i in range(n):
        j = (i+1) % n
        ans += x[i]*y[j] - x[j]*y[i]
    return ans/2

#Function to calculate perimeter of the polygon formed by given vertices
def perimeter(x,y,n):
    ans = 0
    for i in range(n):
        j = (i+1) % n
        ans += dist(x[i],y[i],x[j],y[j])
    return ans

for _ in range(int(input())):
    w,h,n = map(float,input().split())
    x,y,r = [],[],[]
    for i in range(n):
        a,b,c = map(float,input().split())
        x.append(a)
        y.append(b)
        r.append(c)
        
    #Initialization
    ans = 0
    x1,y1,x2,y2,x3,y3,x4,y4 = 0,0,w,0,0,h,w,h
    x = [x1,x2,x3,x4]
    y = [y1,y2,y3,y4]
    ar = area(x,y,4)
    per = perimeter(x,y,4)
    
    for i in range(n):
        #Initialization again
        ans = 0
        x1,y1,x2,y2,x3,y3,x4,y4 = 0,0,w,0,0,h,w,h
        x = [x1,x2,x3,x4]
        y = [y1,y2,y3,y4]
        ar = area(x,y,4)
        per = perimeter(x,y,4)
        #Function to calculate new perimeter and area after removing circle
        def update(x1,y1,x2,y2,x3,y3,x4,y4,x,y,ar,per,r,i):
            #Determining the points of intersection of diagonal of the rectangle and circle
            d = dist(x1,y1,x3,y3)
            if(d <= r[i]):
                #Case when circle lies completely inside the rectangle
                #Area of the new rectangle is zero
                ar = 0
            elif(d >= r[i]):
                #Case when circle lies completely outside the rectangle
                #Perimeter and area of the new rectangle remains same
                per = per
                ar = ar
            else:
                #Case when circle intersects the rectangle at two points
                #Calculating the intersection points
                a = (r[i]*r[i] - d*d + 2*d*d)/(2*d)
                h = math.sqrt(r[i]*r[i] - a*a)
                x5 = x1 + (x3-x1)*a/d
                y5 = y1 + (y3-y1)*a/d
                x6 = x5 + h*(y1-y3)/d
                y6 = y5 - h*(x1-x3)/d
                x7 = x5 - h*(y1-y3)/d
                y7 = y5 + h*(x1-x3)/d
                #Creating vertices
                x = [x1,x2,x3,x4,x6,x7]
                y = [y1,y2,y3,y4,y6,y7]
                #Sorting the vertices in clockwise or anticlockwise order
                #To ensure that a vertex always lies outside the circle
                a = area(x,y,6)
                if(a < 0):
                    x = [x1,x2,x3,x4,x7,x6]
                    y = [y1,y2,y3,y4,y7,y6]
                #Calculating new area and perimeter
                ar = area(x,y,6)
                per = perimeter(x,y,6)
            return ar,per
        
        #Updating perimeter and area after removing the circle
        ar,per = update(x1,y1,x2,y2,x3,y3,x4,y4,x,y,ar,per,r,i)
        ans += per
        ar,per = update(x1,y1,x2,y2,x4,y4,x3,y3,x,y,ar,per,r,i)
        ans += per
        ar,per = update(x1,y1,x3,y3,x4,y4,x2,y2,x,y,ar,per,r,i)
        ans += per
        ar,per = update(x2,y2,x3,y3,x4,y4,x1,y1,x,y,ar,per,r,i)
        ans += per
    print(ans)