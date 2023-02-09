'''


'''

# cook your dish here
def xor(a,b):
    if a==b:
        return 0
    else:
        return 1

def check(a,b):
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and b[i][j]==0:
                return False
    return True

for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    b=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j]=xor(a[i][j],a[j][i])
    if check(a,b):
        for i in b:
            print(*i)
    else:
        print(-1)