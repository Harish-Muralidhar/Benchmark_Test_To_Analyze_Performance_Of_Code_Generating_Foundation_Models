'''


'''

def count_subsequences(l):
    n = len(l)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            if l[i-1]%l[j]==0:
                dp[i]+=dp[j]
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(count_subsequences(l))