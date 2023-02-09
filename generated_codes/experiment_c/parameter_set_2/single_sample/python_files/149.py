'''

'''

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(n):
        if(i==0):
            s=s+l[i]
        else:
            if(l[i]>l[i-1]):
                s=s+l[i]-l[i-1]
    print(s)