'''

'''

#code

t = int(input())
while t:
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        l,b = map(int,input().split())
        a.append(l*b)
    a.sort()
    ans = 0
    for i in range(n-m,n):
        ans += a[i]
    print(ans)
    t -= 1