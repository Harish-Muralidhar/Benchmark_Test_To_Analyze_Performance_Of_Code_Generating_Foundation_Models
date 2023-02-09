'''


'''


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input())
    count = 0
    for i in range(m):
        temp = []
        for j in range(n):
            if a[j][i] == '1':
                temp.append(j)
        for k in range(len(temp)):
            for l in range(k+1, len(temp)):
                count += 1
    print(count)