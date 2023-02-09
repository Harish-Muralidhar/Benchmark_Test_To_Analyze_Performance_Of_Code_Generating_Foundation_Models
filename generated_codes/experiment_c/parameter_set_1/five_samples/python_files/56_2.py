"""
"""

# Write your code here
num_tests = int(input())
for _ in range(num_tests):
    n, k = map(int, input().strip().split())
    if k == 0:
        print(*list(range(1, n+1)))
    elif n == k:
        print(-1)
    else:
        ans = [i for i in range(k+1, n+1)]
        ans.extend(list(range(1, k+1)))
        print(*ans)