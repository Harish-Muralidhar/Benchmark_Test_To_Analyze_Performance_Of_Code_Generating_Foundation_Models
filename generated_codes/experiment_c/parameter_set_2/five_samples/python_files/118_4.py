"""
"""

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    arr.reverse()
    sum = 0
    for i in range(0,n-1,2):
        sum += arr[i]
    print(sum)