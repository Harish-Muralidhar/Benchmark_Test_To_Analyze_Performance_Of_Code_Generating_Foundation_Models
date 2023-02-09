'''

'''

def count_subsequences(n, arr):
    count = 0
    for i in range(2**n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(arr[j])
        if is_valid_subsequence(temp):
            count += 1
    return count

def is_valid_subsequence(arr):
    if len(arr) == 0:
        return False
    if len(arr) == 1:
        if arr[0] == 1:
            return True
        else:
            return False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] != arr[j]:
                if arr[i] > arr[j]:
                    arr[i] -= arr[j]
                else:
                    arr[j] -= arr[i]
    for i in range(len(arr)):
        if arr[i] != 1:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_subsequences(n, arr))