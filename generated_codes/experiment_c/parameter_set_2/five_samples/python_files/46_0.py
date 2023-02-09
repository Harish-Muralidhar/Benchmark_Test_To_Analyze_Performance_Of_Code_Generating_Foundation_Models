"""

"""

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = []
    for j in range(n):
        a.append(list(map(int, input())))
    count = 0
    for j in range(m):
        for k in range(n):
            for l in range(k+1, n):
                if a[k][j] == 1 and a[l][j] == 1:
                    count += 1
    print(count)