'''



'''

n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    for j in range(i+1,n):
        s+=l[i]&l[j]
print(s)