'''

'''

def prob(n,m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    dp[n][m] = 1
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            dp[i][j] = (dp[i+1][j] + dp[i][j+1])/2
    return dp[0][0]

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print(prob(n,m))