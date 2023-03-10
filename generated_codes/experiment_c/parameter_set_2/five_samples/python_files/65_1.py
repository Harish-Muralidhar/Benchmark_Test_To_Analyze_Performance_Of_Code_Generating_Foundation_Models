"""
"""

"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here

# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.First line of each test case has two integer N and M. N lines follow, each has two integers representing the length and breadth of the rectangle.

# Output
# For each test case, output a single line containing the required answer.

# Constraints
# 1 ≤ T ≤ 10^5
# 1 ≤ N ≤ 10^5
# 0 ≤ M ≤ N
# 1 ≤ Rectangle Dimensions ≤ 10^9
# 1 ≤ Sum of N over all test cases ≤ 10^6

# Example
# Input:
# 3
# 1 1
# 10 10
# 2 0
# 5 10
# 5 5
# 2 1
# 1 1
# 2 2

# Output:
# 100
# 25
# 4

# Explanation
# Example case 1
# Abhijeet has only one rectangle. He can remove it, but then the area will be 0. Optimal way is not to remove it. Area = 10 * 10 = 100
# Example case 2
# Abhijeet cannot remove any rectangles in this case. He can however, place them such that the smaller 5 by 5 rectangle is completely inside the larger 5 by 10 rectangle. Then the area of intersection is 5 * 5 = 25
# Example case 3
# Abhijeet can remove atmost 1 rectangles in this case. He can remove the smaller rectangle of size 1 by 1. He is then left with 2 by 2 rectangle of area 4.

# Sample code to perform I/O:

# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

# Write your code