'''


'''

def count_substrings(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j == i + 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 0
    return sum(sum(row) for row in dp)

def count_substrings_2(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j == i + 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 0
    return sum(sum(row) for row in dp)

def count_substrings_3(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j == i + 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
               