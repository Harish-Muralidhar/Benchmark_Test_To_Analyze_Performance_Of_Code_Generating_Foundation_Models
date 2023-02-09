"""

Solution:
"""

import sys
import math

def main():
    test_cases = int(input())
    for i in range(test_cases):
        n, m = map(int, input().split())
        print(n+m-2)

if __name__ == '__main__':
    main()