'''
'''

# Write your code here

def area(a,b,c,d):
    return (c-a)*(d-b)

def max_area(a,b,c,d):
    if a>=c or b>=d:
        return 0
    else:
        return area(a,b,c,d)

def area_intersection(a,b,c,d,e,f,g,h):
    return max_area(a,b,e,f) + max_area(a,b,g,h) + max_area(c,d,e,f) + max_area(c,d,g,h) - max_area(a,b,c,d) - max_area(e,f,g,h)

def solve(a,b,c,d,e,f,g,h,m):
    if m==0:
        return area_intersection(a,b,c,d,e,f,g,h)
    else:
        return max(solve(a,b,c,d,e,f,g,h,m-1),solve(a,b,c,d,e,f,g,h,m-1),solve(a,b,c,d,e,f,g,h,m-1),solve(a,b,c,d,e,f,g,h,m-1))

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a,b,c,d,e,f,g,h=0,0,0,0,0,0,0,0
    for j in range(n):
        a,b=map(int,input().split())
        if a>c:
            c=a
        if b>d:
            d=b
        if a<e:
            e=a
        if b<f:
            f=b
        if a>g:
            g=a
        if b>h:
            h