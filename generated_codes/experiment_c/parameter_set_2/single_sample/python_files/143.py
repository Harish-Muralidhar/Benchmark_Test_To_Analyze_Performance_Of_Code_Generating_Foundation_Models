'''



'''

import sys

def main():
    test_cases = int(input())
    for i in range(test_cases):
        k = int(input())
        s = input()
        n = len(s)
        if n == 1:
            print(0)
            continue
        if k == 1:
            print(0*n)
            continue
        if s.count('?') == 0:
            print(s)
            continue
        if s.count('?') == n:
            print(0*n)
            continue
        if s.count('?') == n-1:
            if s[0] == '?':
                if s[1] == '0':
                    print('1'+s[1:])
                else:
                    print('0'+s[1:])
            else:
                if s[0] == '0':
                    print(s[0]+'1'+s[2:])
                else:
                    print(s[0]+'0'+s[2:])
            continue
        if s.count('?') == n-2:
            if s[0] == '?':
                if s[1] == '0':
                    if s[2] == '0':
                        print('1'+'1'+s[2:])
                    else:
                        print('1'+'0'+s[2:])
                else:
                    if s[2] == '0':
                        print('0'+'1'+s[2:])
                    else:
                        print('0'+'0'+s[2:])
            else:
                if s[0] == '0':
                    if s[n-1] == '0':
                        print(s[0]+'1'+'1')
                    else:
                        print(s[0]+'1'+'0')
                else:
                    if s[n-1] == '0':
                        print(s[0]+'0'+'1')
                    else:
                        print(s[0]+'0'+'