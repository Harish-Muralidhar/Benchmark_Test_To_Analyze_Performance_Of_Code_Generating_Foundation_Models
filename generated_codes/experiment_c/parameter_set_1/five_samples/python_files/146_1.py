'''

'''

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    ans = 0
    for i in range(m):
        if i != 0:
            ans += 1
        for j in arr:
            if j % (m-i) != 0:
                ans += j//(m-i)
            else:
                ans += j//(m-i) - 1
    print(ans)