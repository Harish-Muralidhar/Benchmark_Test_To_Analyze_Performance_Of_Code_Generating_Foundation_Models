'''

'''

# Write your code here
def count_pairs(n, arr):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_pairs(n, arr))