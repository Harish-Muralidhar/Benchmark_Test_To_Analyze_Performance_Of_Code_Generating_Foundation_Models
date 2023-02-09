'''


'''

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    flag = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and x[i][j] == 0:
                flag = 1
                break
    if flag == 1:
        print(-1)
    else:
        for i in range(n):
            for j in range(n):
                if a[i][j] == 0 and x[i][j] == 1:
                    x[i][j] = 0
        for i in range(n):
            for j in range(n):
                print(x[i][j], end = " ")
            print()