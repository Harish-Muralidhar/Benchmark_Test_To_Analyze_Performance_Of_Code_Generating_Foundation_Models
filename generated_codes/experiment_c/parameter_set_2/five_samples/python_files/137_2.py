"""

Explanation
For the first test case the answer is 2 because the expected number of shuffles is 2.

For the second test case the answer is 1826/189.

For the third test case the answer is 877318/35343.

"""

import random
import math

def bogo_sort(n):
    count = 0
    while not is_sorted(n):
        random.shuffle(n)
        count += 1
    return count

def is_sorted(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

def bogo_sort_improved(n):
    count = 0
    while not is_sorted(n):
        random.shuffle(n)
        count += 1
        for i in range(len(n)):
            if n[i] == i+1:
                n[i] = 0
    return count

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def reduce_fraction(n, d):
    gcd_val = gcd(n, d)
    return n//gcd_val, d//gcd_val

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        num_list = [i for i in range(1, n+1)]
        num_list_improved = [i for i in range(1, n+1)]
        count = 0
        for j in range(100000):
            count += bogo_sort(num_list)
        for j in range(100000):
            count += bogo_sort_improved(num_list_improved)
        print(count)
        print(reduce_fraction(count, 200000))

if __name__ == "__main__":
    main()