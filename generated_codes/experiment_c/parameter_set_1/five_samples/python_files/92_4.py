'''

'''

t = int(input())
for _ in range(t):
    n,m,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    num = 0
    for i in range(n):
        num += a[i]
        if num%k == 0:
            if i+1 == m:
                print(num)
                break
        if i+1 == n:
            print(-1)
            break