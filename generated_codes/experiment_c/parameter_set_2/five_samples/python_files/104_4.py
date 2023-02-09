"""

"""

def find_subsequence(s):
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    if count['A'] == count['B']:
        return -1
    else:
        if count['A'] > count['B']:
            return 'B'
        else:
            return 'A'

t = int(input())
for i in range(t):
    s = input()
    print(find_subsequence(s))