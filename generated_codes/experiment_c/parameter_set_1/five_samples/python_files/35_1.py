"""

Explanation
You may refer to the output of the examples displayed after running the test cases.

Testcase 1: Factorial of 3 is 6 (1 x 2 x 3).
Testcase 2: Factorial of 4 is 24 (1 x 2 x 3 x 4).
Testcase 3: Factorial of 5 is 120 (1 x 2 x 3 x 4 x 5).

"""
#program


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    print(factorial(n))