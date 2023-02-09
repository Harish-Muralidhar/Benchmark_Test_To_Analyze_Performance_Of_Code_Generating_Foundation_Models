"""
"""

t = int(input()) 
while t != 0:
    min1, max1 = 0, 0
    s1 = input()
    s2 = input()
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            continue
        else:
            if s1[i] != s2[i]:
                min1 += 1
    s3 = s1.replace("?", "z")
    s4 = s2.replace("?", "a")
    for i in range(len(s1)):
        if s3[i] != s4[i]:
            max1 += 1
    print(min1, max1)
    t -= 1