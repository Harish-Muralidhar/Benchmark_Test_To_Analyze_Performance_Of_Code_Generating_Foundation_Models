"""

"""

import math

def trailing_zeros(n):
    count = 0
    i = 5
    while (n/i >= 1):
        count += int(n/i)
        i *= 5
    return int(count)

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        print(trailing_zeros(n))