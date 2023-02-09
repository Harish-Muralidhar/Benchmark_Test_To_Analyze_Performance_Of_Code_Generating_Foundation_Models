'''

Explanation:

The first number contains 4 occurences of the digit 4 (the first one from the left and three to the right).
The second number contains 0 occurences of the digit 4.
The third number contains 1 occurence of the digit 4 (the last one from the right).
The fourth number contains 1 occurence of the digit 4 (the first one from the left).
The fifth number contains 0 occurences of the digit 4.

'''

# Write your code here

import sys

def count_digit(n):
    count = 0
    while n > 0:
        if n % 10 == 4:
            count += 1
        n //= 10
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(count_digit(n))