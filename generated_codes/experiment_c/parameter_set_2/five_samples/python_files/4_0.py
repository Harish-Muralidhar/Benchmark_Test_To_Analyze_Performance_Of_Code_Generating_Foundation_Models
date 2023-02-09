'''


'''

def subarray(n, arr):
    count = 0
    for i in range(n):
        sum = 0
        product = 1
        for j in range(i, n):
            sum += arr[j]
            product *= arr[j]
            if sum == product:
                count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(subarray(n, arr))