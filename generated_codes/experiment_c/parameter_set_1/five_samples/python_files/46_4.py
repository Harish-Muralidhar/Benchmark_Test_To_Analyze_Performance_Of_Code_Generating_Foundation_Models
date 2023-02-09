'''


'''

#t=int(input())
#for _ in range(t):
#    n,m=map(int(input().split()))
n,m=map(int,input().split())
a=[]
c=0
for _ in range(n):
    a.append(list(input()))
for j in range(m):
    for i in range(n):
        if a[i][j]=='1':
            c+=1
print(c)