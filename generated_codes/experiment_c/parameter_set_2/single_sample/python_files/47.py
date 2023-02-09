'''

Explanation
447474 has 4 occurrences of 4
228 has 0 occurrences of 4
6664 has 1 occurrence of 4
40 has 1 occurrence of 4
81 has 0 occurrences of 4)

'''

# Write your code here

# Importing the required libraries
import math
import os
import random
import re
import sys

# Defining the function to count the number of occurences of 4 in a number
def count_4(n):
    count = 0
    while(n>0):
        if(n%10==4):
            count += 1
        n = n//10
    return count

# Taking the input from the user
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = count_4(n)
        print(result)