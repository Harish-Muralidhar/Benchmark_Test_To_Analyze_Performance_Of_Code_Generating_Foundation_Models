"""
"""

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = [1 for j in range(n)]
    for j in range(n-1):
        if abs(arr[j]) != abs(arr[j+1]) and (arr[j]<0 and arr[j+1]>0) or (arr[j]>0 and arr[j+1]<0):
            res[j+1] = res[j]+1
    print(*res)