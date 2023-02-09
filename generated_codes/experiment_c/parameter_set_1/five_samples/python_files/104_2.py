'''

'''

def f(s):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    for i in d:
        if len(d[i]) == 2:
            return i
    return -1

for _ in range(int(input())):
    s = input()
    print(f(s))