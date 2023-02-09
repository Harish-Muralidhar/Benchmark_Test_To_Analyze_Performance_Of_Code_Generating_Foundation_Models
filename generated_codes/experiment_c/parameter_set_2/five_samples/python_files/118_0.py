"""

Solution:

"""

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    sum = 0
    for i in range(n-1, -1, -2):
        sum += arr[i]
    print(sum)