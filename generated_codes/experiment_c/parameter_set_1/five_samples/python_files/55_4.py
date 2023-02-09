"""
NOTE: The value of N can be as large as 10^5, and so the answer will have to be calculated modulo 10^9 + 7.

"""

import sys
import os
import math

def get_gcd(a, b):
    if a==0:
        return b
    else:
        return get_gcd(b%a, a)

def get_gcd_array(array):
    gcd = array[0]
    for i in array[1:]:
        gcd = get_gcd(gcd, i)
    return gcd

def get_gcd_array_all_subsets(array, n):
    all_gcd = []
    import itertools
    #all_subsets = [[array[j] for j in range(n) if (i&(1<<j))] for i in range(1<<n)]
    for i in range(1<<n):
        subset = array[j] for j in range(n) if (i&(1<<j))
        all_gcd.append(get_gcd_array(subset))
    return all_gcd

def get_product_all_gcd(all_gcd):
    prod = 1
    for i in all_gcd:
        prod *= i
    return prod

# Mod value
mod_val = 1000000007

if __name__ == "__main__":
    # Read the number of test cases
    t = int(raw_input().strip())
    #print t
    # For each test case, get the number of integers and the array of integers
    for a0 in xrange(t):
        # Number of integers
        n = int(raw_input().strip())
        #print n
        # Array of integers
        arr = map(int, raw_input().strip().split(' '))
        #print arr
        all_gcd = get_gcd_array_all_subsets(arr, n)
        prod = get_product_all_gcd(all_gcd)
        #print prod
        print prod%mod_val