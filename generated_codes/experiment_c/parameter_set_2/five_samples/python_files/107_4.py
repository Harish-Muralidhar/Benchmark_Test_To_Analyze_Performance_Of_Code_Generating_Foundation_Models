'''

'''

n,m=map(int,input().split())
l=list(input())
for i in range(m):
    x=int(input())
    b1=0
    b2=0
    for j in range(1,x):
        if int(l[j])-int(l[j-1])>0:
            b1+=int(l[j])-int(l[j-1])
        else:
            b2+=int(l[j])-int(l[j-1])
    print(b1-b2)