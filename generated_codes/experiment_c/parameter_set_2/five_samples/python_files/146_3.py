'''


'''

def minTime(arr):
    n = len(arr)
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr.sort()
    ans = 0
    while arr[0] != arr[-1]:
        ans += 1
        arr[0] += 1
        arr[1] += 1
        arr.sort()
    return ans+1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(minTime(arr))