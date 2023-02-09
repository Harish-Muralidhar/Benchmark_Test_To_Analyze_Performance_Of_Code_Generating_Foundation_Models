"""

Explanation
Test case 1:

In the first round, Captain selects position 1. So the numbering is [1, 0, 1, 2].

Test case 2:

In the first round, Captain selects position 2. So the numbering is [2, 1, 0, 1, 2, 3].
In the second round, Captain selects position 3. So the numbering is [3, 2, 1, 1, 2, 3].

"""

#code

#code

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = [0] + arr
    arr.append(n)
    arr.sort()
    ans = []
    for i in range(1,m+2):
        ans.append(arr[i]-arr[i-1]-1)
    print(*ans)