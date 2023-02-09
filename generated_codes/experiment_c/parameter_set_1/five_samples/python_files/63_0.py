"""


"""
import math

def main():

    t = int(input())
    for _ in range(t):
        w,h,n = map(int, input().split())
        ans = 0
        for _ in range(n):
            x,y,r = map(float, input().split())
            if r==0:
                continue
            x = min(w,max(0, x))
            y = min(h,max(0, y))
            r = min(w,max(0, r))
            m = min(w-x, x, h-y, y)
            if m>=r:
                ans += 4*r
            elif m < r:
                ans += max(2*(m+r), 2*(m-r), 0)
        print(ans)
if __name__ == "__main__":
    main()