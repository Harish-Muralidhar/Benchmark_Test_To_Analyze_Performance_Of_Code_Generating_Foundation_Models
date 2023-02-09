

A:

You can use the following code to solve the problem:
<code>t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for j in range(n-1):
        if a[j] != a[j+1]:
            count += 1
    print(count)
</code>
