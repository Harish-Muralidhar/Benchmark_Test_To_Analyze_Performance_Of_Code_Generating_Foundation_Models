'''


'''

T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    count=0
    for j in range(1,N):
        if A[j]!=A[j-1]:
            count+=1
    print(count)