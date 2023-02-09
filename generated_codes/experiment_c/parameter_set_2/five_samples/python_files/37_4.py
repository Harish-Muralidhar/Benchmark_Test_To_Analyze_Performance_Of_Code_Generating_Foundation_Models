'''


'''
def min_diff(n,m,k):
    if(n>m):
        diff = n-m
        if(diff<=k):
            return 0
        else:
            return diff-k
    else:
        diff = m-n
        if(diff<=k):
            return 0
        else:
            return diff-k

t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    print(min_diff(n,m,k))