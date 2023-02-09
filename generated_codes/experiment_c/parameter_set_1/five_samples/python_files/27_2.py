'''

Explanation

There are 3 test cases. In the first test case, 100 items at 120 dollars means the total expense is 100*120 = 12000 dollars. In the second test case 10 items at 20 dollars means the total expense is 10*20 = 200 dollars. In the third test case, 1200 items at 20 dollars means the total expense is 1200*20 = 21600 dollars.
'''

import sys

def discountCalc(qty, price):
    total = price * qty
    if qty > 1000:
        total *= 0.9
    return total

T = int(input())
for i in range(T):
    qty, price = map(int, input().split())
    print(discountCalc(qty, price))