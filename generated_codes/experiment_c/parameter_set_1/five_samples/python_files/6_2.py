"""

Solution:
"""
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    c1 = 0
    c2 = 0
    for i in range(len(s1)):
        if s1[i]=='?' or s2[i]=='?':
            c1 += 1
        elif s1[i]!=s2[i]:
            c2 += 1
    print(c2,c1+c2)