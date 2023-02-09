'''


'''

#code

t = int(input())
while t>0:
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    c = 0
    for i in range(m):
        b = []
        for j in range(n):
            if a[j][i] == 1:
                b.append(j)
        for k in range(len(b)):
            for l in range(k+1,len(b)):
                c += 1
    print(c)
    t -= 1