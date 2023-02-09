'''

'''

#code

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if k == 0:
        print(*range(1,n+1))
    elif k == n:
        print(-1)
    else:
        for j in range(1,n-k+1):
            print(j+k,end = " ")
        for j in range(1,k+1):
            print(j,end = " ")
        for j in range(n-k+1,n+1):
            print(j,end = " ")
        print()