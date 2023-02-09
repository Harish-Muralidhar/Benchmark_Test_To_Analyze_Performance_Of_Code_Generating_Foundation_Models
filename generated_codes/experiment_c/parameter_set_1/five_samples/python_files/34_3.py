"""
"""


def second_largest(a, b, c):
    if a > b > c or a > c > b:
        return a
    if b > a > c or b > c > a:
        return b
    else:
        return c


test_cases = int(input())
for i in range(test_cases):
    num1, num2, num3 = map(int, input().split())
    print(second_largest(num1, num2, num3))