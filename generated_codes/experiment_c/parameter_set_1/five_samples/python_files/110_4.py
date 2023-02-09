'''

Test Data
Each testcase contains a valid binary string S of length A+E.

Subtasks
Subtask 1: 50 points

1 ≤ T ≤ 100
0 ≤ V ≤ 50
Subtask 2: 50 points

Original constraints
Subtask 3: 50 points

Original constraints

A+E ≤ 5

Subtask 4: 50 points

Original constraints

A+E ≤ 10

'''


def split(s):
    return s[:s.index('E')], s[s.index('E'):]


def hash_func(s):
    result = len(s) - s.count('E')
    if len(s) > 1:
        s1, s2 = split(s)
        result = result + max(hash_func(s1), hash_func(s2))
    return result


def all_binary_strings(a, e, v):
    result = []
    if e == 0:
        if v == a:
            result.append('A' * a)
    elif a == 0:
        if v == e:
            result.append('E' * e)
    else:
        for i in range(1, min(a, v) + 1):
            result += [s + 'A' * i + 'E' * (a - i) for s in all_binary_strings(e, a - i, v - i)]
            result += [s + 'E' * i + 'A' * (a - i) for s in all_binary_strings(e, a - i, v - i)]
    return result


def hash_func_dp(s):
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1 if s[i] == 'A' else 0
    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            dp[i][j] = dp[i][j - 1] + 1 if s[j] == 'A' else dp[i][j - 1]
            if j - i > 1:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)
    return dp[0][len(s) - 1]


result = []
for _ in range(int(input())):
    a, e, v = list(map(int, input().rstrip().split()))
    # result.append(len(all_binary_strings(a, e, v)) % 1000000007)
    result.append(hash_func_dp(a * 'A' + e * 'E'))

for r in result:
    print(r)