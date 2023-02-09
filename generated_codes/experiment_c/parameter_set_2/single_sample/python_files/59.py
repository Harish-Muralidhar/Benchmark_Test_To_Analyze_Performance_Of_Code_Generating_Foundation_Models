'''


'''

def solution(n,a):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            if a[i-1] >= a[j]:
                dp[i] = (dp[i] + dp[j])%1000000009
    return dp[-1]

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(solution(n,a))