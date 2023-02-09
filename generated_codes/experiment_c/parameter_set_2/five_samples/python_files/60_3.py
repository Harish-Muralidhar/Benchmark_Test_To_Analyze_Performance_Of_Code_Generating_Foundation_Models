'''


'''

# Write your code here

def check(n,A,y):
    X = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            X[i][j] = y[i] ^ y[j]
    flag = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1 and X[i][j] == 1:
                flag = 1
                break
    if flag == 1:
        return 0
    else:
        return 1

def solve(n,A):
    y = [0 for i in range(n)]
    for i in range(n):
        if A[i][i] == 1:
            y[i] = 1
    flag = check(n,A,y)
    if flag == 1:
        return y
    else:
        return -1

t = int(input())
for i in range(t):
    n = int(input())
    A = [[0 for i in range(n)] for j in range(n)]
    for j in range(n):
        A[j] = list(map(int,input().split()))
    y = solve(n,A)
    if y == -1:
        print(-1)
    else:
        for i in range(n):
            print(y[i],end = " ")
        print()