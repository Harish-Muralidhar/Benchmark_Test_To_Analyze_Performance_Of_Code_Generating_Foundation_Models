'''

'''

import numpy as np

def find_twice_subseq(s):
    n = len(s)
    dp = np.zeros((n,n))
    for i in range(n):
        dp[i,i] = 1
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j] and l == 2:
                dp[i,j] = 2
            elif s[i] == s[j]:
                dp[i,j] = dp[i+1,j-1] + 2
            else:
                dp[i,j] = max(dp[i,j-1], dp[i+1,j])
    return dp[0,n-1]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(find_twice_subseq(s))