'''

'''

#code

# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    top = list(map(int,input().split()))
    bottom = list(map(int,input().split()))
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if top[i-1] == bottom[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp[n][n])