'''


'''

def area(n,m,rectangles):
    area = 0
    for i in range(n):
        area = area + rectangles[i][0] * rectangles[i][1]
    return area

def areaIntersection(n,m,rectangles):
    if n == m:
        return 0
    else:
        if n > m:
            return area(n-m,m,rectangles)
        else:
            return area(n,m,rectangles)

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    rectangles = []
    for i in range(n):
        arr = list(map(int,input().split()))
        rectangles.append(arr)
    if n == m:
        print(0)
    elif n < m:
        print(0)
    else:
        print(areaIntersection(n,m,rectangles))