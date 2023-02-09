'''

'''

# Write your code here

def solve(n, m):
    if n < m:
        return 0
    if n == m:
        return 1
    if m == 1:
        return 1
    return (solve(n - 1, m - 1) + solve(n - 1, m)) % 1000000009


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        m = int(input())
        print(solve(n, m))