"""

Constraints
1 <= N <= 10^5
1 <= Ai <= 10^9

"""

n = int(input())
arr = list(map(int, input().split()))

def and_sum(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum += arr[i] & arr[j]
    return sum

print(and_sum(arr))