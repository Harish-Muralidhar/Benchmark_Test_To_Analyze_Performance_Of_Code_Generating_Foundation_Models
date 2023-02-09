"""

"""
#t=int(input())
ans = []
for i in range(10):
    n,k,p = map(int,input().split())
    s = 0
    for j in range(1,n+1):
        s += j**k
    ans.append(s%p)
for i in ans:
    print(i)