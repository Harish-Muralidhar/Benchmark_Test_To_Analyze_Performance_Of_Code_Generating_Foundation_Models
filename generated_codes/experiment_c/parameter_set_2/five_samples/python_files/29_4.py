'''

'''

import math
import os
import random
import re
import sys

# Complete the function below.

def calculate_gross_salary(basic_salary):
    if basic_salary < 1500:
        hra = basic_salary * 0.1
        da = basic_salary * 0.9
    else:
        hra = 500
        da = basic_salary * 0.98
    gross_salary = basic_salary + hra + da
    return gross_salary

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        basic_salary = int(input())

        result = calculate_gross_salary(basic_salary)

        fptr.write(str(result) + '\n')

    fptr.close()