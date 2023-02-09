'''
Required sum = 6.0

'''

import sys

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        print(n + m - 1)

if __name__ == "__main__":
    main()