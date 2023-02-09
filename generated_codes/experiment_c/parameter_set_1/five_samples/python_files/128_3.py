"""
"""

t = int(input())
for i in range(t):
    s = input()
    k = int(input())
    sl = list(s)
    sl.sort()
    res = ""
    for i in range(k):
        res += sl[i]
    print(res)