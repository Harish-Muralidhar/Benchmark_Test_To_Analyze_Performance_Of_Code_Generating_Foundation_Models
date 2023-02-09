'''

'''

for i in range(int(input())):
    n,k,e,m = map(int,input().split())
    a = []
    for j in range(n-1):
        a.append(list(map(int,input().split())))
    s = list(map(int,input().split()))
    a.sort(key=lambda x:sum(x[:-1]))
    if sum(a[-k][:-1]) - sum(s) + 1 <= m:
        print(sum(a[-k][:-1]) - sum(s) + 1)
    else:
        print("Impossible")