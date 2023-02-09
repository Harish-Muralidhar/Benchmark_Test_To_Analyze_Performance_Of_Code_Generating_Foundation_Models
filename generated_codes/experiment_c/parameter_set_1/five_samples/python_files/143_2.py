'''



'''

import sys

def fill(s, n, k):
    tmp = s[0]
    for i in range(n):
        if s[i] == '?':
            if ord(tmp) - ord('0') + 1 < k:
                s[i] = chr(ord(tmp) + 1)
                tmp = s[i]
            else:
                s[i] = '0'
                tmp = s[i]
        else:
            tmp = s[i]

    return s

def solve():
    T = int(input())
    for i in range(T):
        k = int(input())
        s = list(input())
        n = len(s)
        if n == 1:
            print('0')
        else:
            for i in range(n):
                if s[i] == '?':
                    s[i] = '0'
            for i in range(n):
                if s[i] == s[(i + 1) % n]:
                    s = fill(s, n, k)
                    break

            if s[-1] == s[0]:
                print('NO')
            else:
                print(''.join(s))


if __name__ == '__main__':
    sys.stdin = open('input.txt')
    solve()