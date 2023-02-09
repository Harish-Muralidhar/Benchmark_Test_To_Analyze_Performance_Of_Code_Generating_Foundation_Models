"""

"""

n = int(input())
a = list(map(int, input().split()))

#print(a)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += a[i] & a[j]

print(ans)