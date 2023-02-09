'''


'''

t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    csum=0
    cprod=1
    for i in range(n):
        if a[i]==0:
            csum=0
            cprod=1
        else:
            csum+=a[i]
            cprod*=a[i]
        if csum==cprod:
            res+=1
    print(res)