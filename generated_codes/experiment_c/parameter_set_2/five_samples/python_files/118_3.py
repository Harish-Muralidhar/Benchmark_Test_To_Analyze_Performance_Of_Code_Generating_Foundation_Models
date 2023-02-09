'''

'''

#code

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    s = 0
    for i in range(n-1,-1,-2):
        s += l[i]
    print(s)