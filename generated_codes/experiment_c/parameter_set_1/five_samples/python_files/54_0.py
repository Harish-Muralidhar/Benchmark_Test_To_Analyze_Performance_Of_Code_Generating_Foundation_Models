"""
"""

#code
t = int (input())
for i in range(t):
    n = int(input())
    e, o = input().split()
    e = int(e)
    o = int(o)
    l = []
    if n%2 == 0:
        if e == n*(n+1)//2:
            print("-1")
        else:
            e -= n//2
            o+= n//2
            for i in range(n):
                if i%2 == 0:
                    l.append("1")
                else:
                    l.append("2")
            for i in range(len(l)):
                if l[i] == "2":
                    if e!=0:
                        l[i] = "1"
                        e -= 1
                    else:
                        break
            print(*l)
    else:
        if e == 0:
            print("-1")
        else:
            e -= n//2
            o += n//2
            for i in range(n):
                if i%2 == 0:
                    l.append("1")
                else:
                    l.append("2")
            for i in range(len(l)):
                if l[i] == "2":
                    if e!=0:
                        l[i] = "1"
                        e -= 1
                    else:
                        break
            print(*l)