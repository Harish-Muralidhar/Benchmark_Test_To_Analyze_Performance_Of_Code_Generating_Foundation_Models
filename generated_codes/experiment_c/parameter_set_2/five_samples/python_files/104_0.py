"""

"""

#code

t = int(input())
while t>0:
    s = input()
    l = len(s)
    d = {}
    for i in range(l):
        d[i] = []
    for i in range(l):
        for j in range(l):
            if s[i] == s[j]:
                d[i].append(j)
    for i in range(l):
        for j in range(l):
            if len(d[i]) == 2:
                if d[i][0] == d[i][1]:
                    print(s[i])
                    break
            else:
                print(-1)
                break
    t = t-1