"""

"""


# n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        count += a[i] & a[j]

print(count)