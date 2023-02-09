'''

'''

import sys

def main():
    test_case = int(sys.stdin.readline())
    for i in range(test_case):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')

if __name__ == '__main__':
    main()