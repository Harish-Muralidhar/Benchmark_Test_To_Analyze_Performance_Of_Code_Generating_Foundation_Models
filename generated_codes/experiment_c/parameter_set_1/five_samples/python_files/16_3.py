'''


'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    g=a[0]
    for i in range(1,len(a)):
        g=gcd(g,a[i])
    if k>g:
        print(-1)
    else:
        c=0
        for i in range(len(a)):
            x=a[i]%k
            if x==0:
                continue
            else:
                y=(x+k)//2
                if x>y:
                    c+=(x-y)
                else:
                    c+=(y-x)
        print(c)