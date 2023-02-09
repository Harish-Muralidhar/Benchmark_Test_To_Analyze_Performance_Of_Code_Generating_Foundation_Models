'''

Explanation

Test Case 1

There is only one round. Position selected by Captain is 1. So the numbering will be [1, 0, 1, 2].

Test Case 2

There are two rounds. In the first round, position selected by Captain is 2. So the numbering will be [2, 1, 0, 1, 2, 3]. In the second round, position selected by Captain is 3. So the numbering will be [3, 2, 1, 1, 2, 3].

'''

# Write your code here

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = [0]*n
    for j in range(m):
        res[arr[j]] = n-arr[j]
        for k in range(arr[j]-1, -1, -1):
            res[k] = res[k+1] + 1
        for k in range(arr[j]+1, n):
            res[k] = res[k-1] - 1
    print(*res)