"""

Solution :
"""
for _ in range(int(input())):
    n,m=map(int,input().split())
    pos=list(map(int,input().split()))
    arr=[0]*n
    for i in range(m):
        arr[pos[i]:]=arr[:pos[i]][::-1]
    print(*arr)