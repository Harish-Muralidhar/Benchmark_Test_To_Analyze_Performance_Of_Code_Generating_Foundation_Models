'''

'''

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if(len(set(l))==1):
        print("NO")
    elif(len(set(l))<=k):
        print("YES")
    else:
        print("NO")