"""

"""

# my solution:

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    d = []
    for j in range(len(a)):
        if j == 0:
            c += 1
            d.append(a[0])
        elif a[j] < d[-1]:
            d.append(a[j])
        else:
            c += 1
            d.append(a[j])
    print(c)