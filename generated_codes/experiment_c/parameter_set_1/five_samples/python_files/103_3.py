"""

Explanation
For the first case, 4^4 = 256 = 25 56.
"""
import math

t = int(input("Number of test cases: "))

while t > 0:
    n, k = map(int, input("Please enter two numbers separated by spaces: ").split())

    print(str(int(str(n**n)[:k])), str(int(str(n**n)[-k:])))
    t -= 1