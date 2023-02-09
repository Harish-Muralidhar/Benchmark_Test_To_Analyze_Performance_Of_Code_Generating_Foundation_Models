'''


'''

# Write your code here
import math
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    g=math.gcd(l[0],l[1])
    for j in range(2,len(l)):
        g=math.gcd(g,l[j])
    c=0
    for j in range(len(l)):
        if l[j]%g==0 and l[j]%k==0:
            c=c+0
        elif l[j]%g==0 and l[j]%k!=0:
            c=c+(k-l[j]%k)
        elif l[j]%g!=0 and l[j]%k!=0:
            c=c+(g-l[j]%g)+(k-l[j]%k)
        elif l[j]%g!=0 and l[j]%k==0:
            c=c+(g-l[j]%g)
    print(c)