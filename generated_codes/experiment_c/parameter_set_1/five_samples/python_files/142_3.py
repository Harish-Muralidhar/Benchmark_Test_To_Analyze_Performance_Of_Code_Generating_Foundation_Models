"""
a1 = b1 = 0
ai = bi = N for some i
ai+1 = ai + 1 for all i
bi+1 = bi + 1 for all i

"""

for _ in range(int(input())):
    n = int(input())
    a = [0]*(n+1)
    b = [0]*(n+1)
    for i in range(1,n+1):
        a[i],b[i] = map(int,input().split())
    a[0] = 0
    b[0] = 0
    dp = [[0]*(n+1) for i in range(n+1)]

    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(b[i]+1):
            if j >= a[i]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
    ans = dp[n][b[n]]
    is_knave = [0]*(n)
    for i in range(n,0,-1):
        if b[i]>=a[i]:
            if dp[i-1][b[i]-1]!=0:
                is_knave[i-1] = 1
                b[i-1] = b[i]-1
            else:
                is_knave[i-1] = 0
                b[i-1] = b[i]
        else:
            is_knave[i-1] = 0
            b[i-1] = b[i]
    print(ans)
    for i in range(n):
        print(is_knave[i],end="")
    print()