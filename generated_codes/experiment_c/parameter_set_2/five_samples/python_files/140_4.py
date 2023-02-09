'''


'''

def countWays(n): 
    dp = [0 for i in range(n + 1)] 
    dp[0] = dp[1] = 1
    for i in range(2, n + 1): 
        dp[i] = dp[i - 1] + dp[i - 2] 
    return dp[n] 
  
# Driver code 
n = int(input())
for i in range(n):
    print(countWays(int(input())))