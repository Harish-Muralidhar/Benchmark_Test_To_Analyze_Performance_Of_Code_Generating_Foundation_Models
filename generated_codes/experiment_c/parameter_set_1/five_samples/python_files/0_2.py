'''

'''

def hammDist(str1, str2):
    d = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            d += 1
    return d

tc = int(raw_input())
while tc > 0:
    s1 = raw_input()
    s2 = raw_input()
    n = len(s1)
    max_hd = 0
    pref = ''
    for i in range(n):
        diff = hammDist(s1[0:i+1], s2[0:i+1])
        if diff > max_hd:
            max_hd = diff
            pref = s1[0:i+1]
    res = ''
    for i in range(n):
        if i < len(pref):
            res += pref[i]
        else:
            if pref[-1] == 'B':
                res += 'W'
            else:
                res += 'B'
    print res
    tc -= 1