'''

'''

import math

def area(a,b,c,d):
    return abs((c-a)*(d-b))

def find_area(a,b,c,d,e,f,g,h):
    x1 = max(a,e)
    y1 = max(b,f)
    x2 = min(c,g)
    y2 = min(d,h)
    if x1>=x2 or y1>=y2:
        return 0
    else:
        return area(x1,y1,x2,y2)

def max_area(a,b,c,d,e,f,g,h):
    return max(area(a,b,c,d),area(e,f,g,h),find_area(a,b,c,d,e,f,g,h))

def main():
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        if m==0:
            print(max_area(a[0],a[1],a[2],a[3],b[0],b[1],b[2],b[3]))
        else:
            print(max(area(a[0],a[1],a[2],a[3]),area(b[0],b[1],b[2],b[3])))

if __name__ == '__main__':
    main()