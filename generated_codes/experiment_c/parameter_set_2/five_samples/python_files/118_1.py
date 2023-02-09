"""
"""

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    sum = 0
    for i in range(n-1, -1, -2):
        sum += l[i]
    print(sum)