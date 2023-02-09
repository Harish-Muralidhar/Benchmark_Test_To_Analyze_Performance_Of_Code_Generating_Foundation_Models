"""

"""

# Write your code here

import sys

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

if __name__ == '__main__':
    test_cases = int(sys.stdin.readline())
    for test_case in range(test_cases):
        num = int(sys.stdin.readline())
        print(sum_of_digits(num))