'''

'''

#code
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    l = []
    for j in range(n):
        l.append(list(map(int,input())))
    c = 0
    for j in range(m):
        c1 = 0
        for k in range(n):
            if l[k][j] == 1:
                c1 += 1
        c += (c1*(c1-1))//2
    print(c)