"""


"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for _ in range(m):
        g,x,y = map(int,input().split())
        s = []
        for i in range(x-1,y):
            if gcd(g,a[i])>1:
                s.append(a[i])
        if len(s) == 0:
            print(-1,-1)
        else:
            print(max(s),s.count(max(s)))

main()