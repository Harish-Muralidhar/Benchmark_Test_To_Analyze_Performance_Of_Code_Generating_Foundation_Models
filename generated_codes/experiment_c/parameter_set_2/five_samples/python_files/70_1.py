"""

"""

t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(*arr)