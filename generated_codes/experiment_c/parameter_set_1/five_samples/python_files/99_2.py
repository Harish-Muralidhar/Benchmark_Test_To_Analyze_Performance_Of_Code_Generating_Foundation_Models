'''

Author: 
Md. Ismail,
Rajshahi University of Engineering and Technology

Date: 
28/10/2019
'''

def longest_shared_subsequence(A, B):
    m, n = len(A), len(B)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if A[i]==B[j]:
                dp[i+j][j+1] = dp[i][j]+1
    return max(dp[-1])

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(longest_shared_subsequence(A, B))