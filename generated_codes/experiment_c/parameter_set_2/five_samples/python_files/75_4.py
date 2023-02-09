"""

"""

def is_possible(n, k, arr):
    for i in range(n):
        if arr[i]%k == 0:
            arr[i] = arr[i]//k
        else:
            arr[i] = arr[i]//k + 1
    return sum(arr) == n-1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if is_possible(n, k, arr):
        print("YES")
    else:
        print("NO")