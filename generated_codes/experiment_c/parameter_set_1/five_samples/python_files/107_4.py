


A:

Here is my answer:
<code>def chef_and_party(n, m, a):
    res = []
    for x in m:
        b1 = 0
        b2 = 0
        for y in range(1, x):
            by = a[x-1] - a[y-1]
            if by &gt; 0:
                b1 += by
            else:
                b2 += by
        res.append(b1+b2)
    return res

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    a = list(map(int, list(input())))
    m = list(map(int, input().split()))
    print(*chef_and_party(n, m, a))
</code>
