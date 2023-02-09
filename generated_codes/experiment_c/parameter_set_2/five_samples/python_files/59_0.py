"""

"""

# Write your code here

def count_seq(arr, n):
    if n == 0:
        return 1
    if arr[n-1] == 0:
        return count_seq(arr, n-1)
    else:
        return (count_seq(arr, n-1) + count_seq(arr, arr[n-1]))%1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_seq(arr, n))