'''



'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    s = input().strip()
    if k == 1:
        print(s.replace('?', '0'))
        continue
    if k == 2:
        s = s.replace('?', '0')
        if s[0] == s[-1]:
            print(s[1:] + s[0])
        else:
            print(s)
        continue
    if k == 3:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print(s[:-1] + '1')
        else:
            print(s)
        continue
    if k == 4:
        s = s.replace('?', '0')
        if s[0] == s[-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue
    if k == 5:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue
    if k == 6:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue
    if k == 7:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue
    if k == 8:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue
    if k == 9:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue
    if k == 10:
        s = s.replace('?', '0')
        if s == s[::-1]:
            print('NO')
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + '1' + s[i + 1:]
                break
        print(s)
        continue