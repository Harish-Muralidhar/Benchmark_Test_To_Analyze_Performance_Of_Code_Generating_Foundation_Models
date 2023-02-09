'''

'''

import math

mod = 1000000007

for _ in range(int(input())):
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        inp = input().split()
        a[i] = int(inp[0])
        b[i] = int(inp[1])
    ans = []
    ans2 = []
    min_ans = 0
    max_ans = 0
    for i in range(n):
        min_ans = max(min_ans, a[i])
        max_ans = min(max_ans, b[i])
    for i in range(min_ans, max_ans + 1):
        ans.append(i)
        ans2.append(bin(i))
    print(len(ans))
    print(ans2[0])