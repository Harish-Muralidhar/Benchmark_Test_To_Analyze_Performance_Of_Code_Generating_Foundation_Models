"""


"""

# Write your code here
import math

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    gcd = a[0]
    for j in range(1, len(a)):
        gcd = math.gcd(gcd, a[j])
    if gcd == 1:
        print(-1)
    else:
        print(a[0] - gcd)