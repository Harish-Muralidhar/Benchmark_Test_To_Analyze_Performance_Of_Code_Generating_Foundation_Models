'''


'''

def xor(a,b):
    if a==b:
        return 0
    else:
        return 1

def check(a,b):
    for i in range(n):
        for j in range(n):
            if a[i][j]==0 and b[i][j]==1:
                return False
    return True

def check2(a,b):
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and b[i][j]==0:
                return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    b=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j]=xor(i,j)
    if check(a,b) and check2(a,b):
        for i in range(n):
            print(i,end=" ")
        print()
    else:
        print(-1)