"""
So the lexicographically smallest arrangement for Z which maximizes the value is BWBW.
"""

def hammingDistance(str1,str2):
    dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dist += 1
    return dist

def sol(str1,str2):
    str3 = ''
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            str3 += str1[i]
        else:
            if str1[i] == 'W':
                str3 += 'B'
            else:
                str3 += 'W'
    return str3

t = int(input())
for i in range(t):
    str1 = input()
    str2 = input()
    print(sol(str1,str2))