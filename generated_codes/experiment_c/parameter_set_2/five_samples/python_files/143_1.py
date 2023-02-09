'''



'''

import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        k = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        print(solve(k,s))

def solve(k,s):
    if len(s) == 1:
        if s == '?':
            return '0'
        else:
            return s
    if len(s) == 2:
        if s == '??':
            return '01'
        elif s[0] == '?':
            if s[1] == '0':
                return '1' + s[1]
            else:
                return '0' + s[1]
        elif s[1] == '?':
            if s[0] == '0':
                return s[0] + '1'
            else:
                return s[0] + '0'
        else:
            return 'NO'

    if s[0] == '?':
        for i in range(k):
            if i != int(s[1]):
                s = str(i) + s[1:]
                break
    if s[-1] == '?':
        for i in range(k):
            if i != int(s[-2]):
                s = s[:-1] + str(i)
                break
    for i in range(1,len(s)-1):
        if s[i] == '?':
            for j in range(k):
                if j != int(s[i-1]) and j != int(s[i+1]):
                    s = s[:i] + str(j) + s[i+1:]
                    break
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return 'NO'
    if s[0] == s[-1]:
        return 'NO'
    return s

if __name__ == '__main__':