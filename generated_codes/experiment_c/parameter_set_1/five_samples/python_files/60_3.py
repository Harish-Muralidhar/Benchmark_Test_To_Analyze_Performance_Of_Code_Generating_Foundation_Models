'''

'''

T = int(input())
for t in range(T):
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    flag = 1
    y = [0]*N
    for i in range(N):
        if A[i][i] == 0:
            continue
        else:
            flag = 0
            break
    if flag == 0:
        print(-1)
        continue
    else:
        for i in range(N):
            if A[i][(i+1)%N] == 0:
                y[i] = 0
            else:
                y[i] = 1
        print(*y)