'''

'''


T = int(input())
for i in range(T):
    num = input().split()
    n = int(num[0])
    k = int(num[1])
    arr = input().split()
    arr = list(map(int,arr))
    diff = []
    for i in range(n):
        diff.append(k-arr[i])
    arr.sort()
    diff.sort()
    if arr == diff:
        print("YES")
    else:
        print("NO")