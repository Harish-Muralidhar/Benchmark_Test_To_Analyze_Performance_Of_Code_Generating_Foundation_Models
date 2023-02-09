'''

Explanation
Example case 1.

In the first round, Captain selects position 1. The numbering will be [1, 0, 1, 2].

Example case 2.

In the first round, Captain selects position 2. The numbering will be [2, 1, 0, 1, 2, 3].
In the second round, Captain selects position 3. The numbering will be [3, 2, 1, 1, 2, 3].

'''

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [0] + arr + [n]
    arr.sort()
    res = [0]*(n+1)
    for i in range(1, m+2):
        res[arr[i-1]+1:arr[i]+1] = list(range(arr[i-1], arr[i], -1))
    print(*res[1:])