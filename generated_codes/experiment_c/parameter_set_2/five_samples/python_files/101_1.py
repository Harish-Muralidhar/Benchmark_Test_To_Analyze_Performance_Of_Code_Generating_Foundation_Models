'''


Explanation

In the first test case, the beanstalk can grow in the following way:

Level 1: 1 stem, 0 leaves
Level 2: 1 stem, 1 leaf
Level 3: 1 stem, 2 leaves
In the second test case, there is no way for the beanstalk to grow in accordance with the Bytelandian rules.

'''

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_valid(n):
    if n == 0:
        return True
    if is_prime(n):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if not is_valid(i) or not is_valid(n/i):
                return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if is_valid(arr[-1]):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()