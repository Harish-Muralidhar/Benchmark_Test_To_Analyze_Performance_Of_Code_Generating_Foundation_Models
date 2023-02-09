"""

"""

T = int(input())

for i in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for j in a:
        b.append(abs(j-k))
    diff = min(b)
    print(diff, b.count(diff))