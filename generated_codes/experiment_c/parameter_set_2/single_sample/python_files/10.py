'''

Explanation
The optimal way is to move from 1-st to 3-rd street, and then to 4-th street. The product will be equal to 1 * 2 * 4 = 8.

'''

def main():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            if i == 1:
                dp[i][j] = arr[i-1]
            else:
                if i-j-1 < 0:
                    dp[i][j] = dp[i-1][j]*arr[i-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-j-1][j]*arr[i-1])
    print(dp[n][k])

if __name__ == '__main__':
    main()