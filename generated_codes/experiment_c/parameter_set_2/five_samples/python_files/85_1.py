'''
'''

#Solution

import sys

def main():
    n = int(input())
    for i in range(n):
        a, b, c = [int(x) for x in input().split()]
        print(min(b, c) - 1 + max(b, c) - min(b, c) + 1)

if __name__ == "__main__":
    main()