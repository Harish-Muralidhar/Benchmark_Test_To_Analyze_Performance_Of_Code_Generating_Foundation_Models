'''

Study Python Functions in the following link:

https://www.w3schools.com/python/python_functions.asp

https://www.programiz.com/python-programming/function

https://www.tutorialspoint.com/python/python_functions.htm

Reference:

https://www.hackerrank.com/challenges/write-a-function/problem
'''

#Program

import math

def factorial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    return math.factorial(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = factorial(n)

        fptr.write(str(result) + '\n')

    fptr.close()