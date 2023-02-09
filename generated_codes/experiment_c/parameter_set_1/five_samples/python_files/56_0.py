'''

'''


t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    
    if 2*k>=n:
        print(-1)
    else:
        for j in range(1,n+1):
            print(j+k,end=" ")
        print()