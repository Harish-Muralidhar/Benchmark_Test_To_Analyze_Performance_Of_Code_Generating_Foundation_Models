'''


'''
def change_to_one(arr, n):
    if n <= 0:
        return 1
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            arr[j] -= arr[i]
            count += change_to_one(arr, n - 1)
    return count

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(change_to_one(arr, n))