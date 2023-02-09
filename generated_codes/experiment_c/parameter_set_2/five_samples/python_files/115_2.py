"""

"""

# Write your code here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    while len(set(arr)) != 1:
        arr.sort()
        arr[-1] = arr[-1] - arr[-2]
        arr = arr[:-1]
    print(arr[0])