'''

'''

t = int(input())
for i in range(t):
    n,k,p = map(int,input().split())
    sum = 0
    for j in range(1,n+1):
        sum += j**k
    print(sum%p)