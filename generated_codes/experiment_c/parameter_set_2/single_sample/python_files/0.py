"""
So, the answer is "BWBW".
"""

#code

for i in range(int(input())):
    s1 = input()
    s2 = input()
    c1 = 0
    c2 = 0
    for i in range(len(s1)):
        if s1[i] == 'W':
            c1 += 1
        if s2[i] == 'W':
            c2 += 1
    if c1 > c2:
        print('B'*c2 + 'W'*(len(s1)-c2))
    else:
        print('B'*c1 + 'W'*(len(s1)-c1))