'''

'''

n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
    k = int(input())
    a.sort()
    cost = 0
    for i in range(n):
        if k == 0:
            cost += a[i]
        else:
            cost += a[i]
            k -= 1
    print(cost)