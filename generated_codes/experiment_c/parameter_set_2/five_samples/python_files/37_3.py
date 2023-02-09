"""


"""



def min_diff(n,m,k):
    diff = abs(n-m)
    if diff == 0:
        return 0
    if k >= diff:
        return 0
    else:
        return diff-k

t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    print(min_diff(n,m,k))