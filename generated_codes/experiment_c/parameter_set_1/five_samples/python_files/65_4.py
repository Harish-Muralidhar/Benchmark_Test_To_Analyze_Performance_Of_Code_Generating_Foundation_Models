"""

Solution:
"""

for _ in range(int(input())):
    n,m = map(int,input().split())
    l =[]
    for i in range(n):
        r = list(map(int,input().split()))
        l.append(r)
    l.sort()
    s = 0
    while m and l:
        m-=1
        l.pop()
        if l:
            s = max(s,l[-1][0]*l[-1][1])
    print(s)