"""


Input:
2
2 2
3 3

Output:
4
26
"""
import math
MOD = 531169

t = int(input("Enter the number of test cases: "))
for _ in range(t):
    a, b = map(int, input("Enter the values of a and b: ").split())
    C = (math.factorial(a + b) // (math.factorial(a) * math.factorial(b))) % MOD
    print("The number of prime words which can be built from exactly {} ones and {} zeros is {}.".format(a, b, C))