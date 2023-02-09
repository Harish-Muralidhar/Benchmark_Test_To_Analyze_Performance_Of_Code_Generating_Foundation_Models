"""


"""

import sys

def get_input():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        s = list(map(int, input().split()))
        t = list(map(int, input().split()))
        yield (n, s, t)

def solve(n, s, t):
    #print(n, s, t)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        if s[i] < t[i]:
            a[s[i]] = 1
            b[t[i]] = 1
        else:
            a[t[i]] = 1
            b[s[i]] = 1
    #print(a, b)
    return ''.join(['A' if a[i] == 1 else 'B' for i in range(n)])

def main():
    for n, s, t in get_input():
        print(solve(n, s, t))

if __name__ == '__main__':
    main()