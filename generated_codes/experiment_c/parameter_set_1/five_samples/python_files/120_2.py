'''
'''

# Write your code here
import math

def find_prob(n,m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            else:
                p = dp[i][j-1]/2.0
                q = dp[i-1][j]/2.0
                dp[i][j] = p + q
    return math.floor(sum(sum(x) for x in dp))

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        n,m = map(int,input().split())
        print("{0:.6f}".format(find_prob(n,m)))