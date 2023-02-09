'''

'''

t = int(input())

for i in range(t):
    n,k,e,m = map(int,input().split())
    a = []
    for j in range(n-1):
        a.append(list(map(int,input().split())))
    b = list(map(int,input().split()))
    a.append(b)
    a.sort(key=lambda x:sum(x))
    if sum(a[n-k-1])-sum(b)>m-e:
        print("Impossible")
    else:
        print(m-sum(a[n-k-1])+sum(b))