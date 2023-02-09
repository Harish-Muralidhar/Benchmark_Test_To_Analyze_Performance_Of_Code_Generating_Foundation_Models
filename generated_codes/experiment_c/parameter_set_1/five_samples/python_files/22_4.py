'''

Explanation
Test Case 1: Sum of first digit and last digit of 1234 is 1 + 4 = 5.

Test Case 2: Sum of first digit and last digit of 124894 is 1 + 4 = 5.

Test Case 3: Sum of first digit and last digit of 242323 is 2 + 3 = 5.

'''

#Program Code:

def digit_sum(n):
    return n if n < 10 else n%10 + digit_sum(n//10)

try:
    t = int(input())
    for i in range(t):
        n = int(input())
        print(digit_sum(n))
except:
    pass