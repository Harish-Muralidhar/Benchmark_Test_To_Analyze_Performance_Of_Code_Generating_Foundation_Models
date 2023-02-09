'''

Explanation of the sample testcase
The optimal way is to move from 1-st to 2-nd, then from 2-nd to 4-th street. The product will be equal to 2 * 4 = 8, which is the answer.

'''

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    if n==1:
        print(a[0])
        return
    if k==1:
        print(min(a))
        return
    if k==n:
        print(max(a))
        return
    dp = [0]*(n+1)
    dp[1] = a[0]
    dp[2] = a[1]
    for i in range(3,n+1):
        dp[i] = min(dp[i-j]*a[i-1] for j in range(1,k+1))
    print(dp[n])

if __name__ == '__main__':
    main()