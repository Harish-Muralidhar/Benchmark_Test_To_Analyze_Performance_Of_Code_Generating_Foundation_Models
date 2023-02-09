"""

"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = 0
    for i in range(n):
        if a[i]-b[i] >= c:
            c = a[i]
        else:
            break
    print(i+1)