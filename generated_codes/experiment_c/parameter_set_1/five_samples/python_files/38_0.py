'''

Explanation:
Input: 10
Output: 3 (the square root of 10 is 3.32....)

Input: 5
Output: 2 (the square root of 5 is 2.23....)

Input: 10000
Output: 100 (the square root of 10000 is 100.00)
'''

# Write your code here
import math
T = int(input())
for i in range(T):
    x = int(input())
    print(math.floor(math.sqrt(x)))