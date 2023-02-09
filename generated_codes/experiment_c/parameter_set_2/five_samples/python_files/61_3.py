"""

Note: The solution will be accepted if it is correct and the score is at least 50 points.

"""

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += a[i] & a[j]

print(ans)