"""
"""
# cook your dish here
t = int(input())
for i in range(t):
    a = input()
    b = input()
    min_diff = 0
    for j, k in zip(a, b):
        if j == '?' or k =='?':
            continue
        if j != k:
            min_diff += 1
    max_diff = min_diff
    for j, k in zip(a, b):
        if j == '?' and k == '?':
            max_diff += 2
        elif j == '?' or k == '?':
            max_diff += 1
    print(min_diff, max_diff)