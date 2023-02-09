'''

Explanation

In the first test case, 1 divided by 2 leaves a remainder 1.
In the second test case, remainder when 100 is divided by 200 is 100.
In the third test case, remainder when 10 is divided by 40 is 10.

'''

import sys

def main():
    test_cases = int(sys.stdin.readline().strip())
    for i in range(test_cases):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(a % b)

if __name__ == '__main__':
    main()