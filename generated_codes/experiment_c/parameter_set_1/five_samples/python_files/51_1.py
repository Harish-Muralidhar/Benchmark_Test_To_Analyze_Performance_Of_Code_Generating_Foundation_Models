"""

Explanation

In the first case, the bonus should be given as 140, 120, 100 and 100 to employees 1, 2, 3 and 4 respectively.
"""

t = int(input())
for i in range(t):
    n,m,l = map(int, input().split())
    a = [[0]*(n+1) for i in range(n+1)]
    for j in range(m):
        i,j,c = map(int, input().split())
        a[i][j] = -c
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                a[i][j] = max(a[i][j], a[i][k] + a[k][j])
    
    for i in range(1, n+1):
        if a[i][i] < 0:
            print("Inconsistent analysis.")
            break
    else:
        dp = [l]*(n+1)
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                dp[j] = max(dp[j], dp[i]+a[i][j])
        print(sum(dp))
        print(" ".join([str(i) for i in dp]))