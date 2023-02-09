'''

'''


from sys import stdin,stdout
n=int(stdin.readline().strip())
a=list(map(int,stdin.readline().strip().split()))
q=int(stdin.readline().strip())
for i in range(q):
    k=int(stdin.readline().strip())
    b=[0]*(k+1)
    c=[0]*(k+1)
    b[0]=a[0]
    c[0]=a[0]
    for j in range(1,k+1):
        b[j]=max(b[j-1],a[j])
        c[j]=b[j]+c[j-1]
    for j in range(k+1,n):
        b[0]=a[j]+c[k]
        c[0]=a[j]+c[k]
        for l in range(1,k+1):
            b[l]=max(b[l-1],a[j]+c[k-l])
            c[l]=b[l]+c[l-1]
    stdout.write(str(c[k])+"\n")