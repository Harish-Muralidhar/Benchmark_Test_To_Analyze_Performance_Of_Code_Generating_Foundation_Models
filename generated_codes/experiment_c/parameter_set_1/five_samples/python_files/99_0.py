'''

'''
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n+1):
            if A[i:j]==B[i:j]:
                if j-i>c:
                    c=j-i
    print(c)