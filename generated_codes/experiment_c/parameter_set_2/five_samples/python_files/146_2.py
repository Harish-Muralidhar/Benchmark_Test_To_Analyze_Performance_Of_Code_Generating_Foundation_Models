"""


"""

# Write your code here

def min_time(arr):
    n = len(arr)
    arr.sort()
    res = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and arr[j] == arr[i]:
            j += 1
        res += (j - i) * arr[i]
        i = j
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_time(arr))