'''

'''

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def get_gcd(arr):
    gcd_val = arr[0]
    for i in range(1, len(arr)):
        gcd_val = gcd(gcd_val, arr[i])
    return gcd_val

def get_lcm(arr):
    lcm_val = arr[0]
    for i in range(1, len(arr)):
        lcm_val = lcm(lcm_val, arr[i])
    return lcm_val

def get_product(arr):
    product = 1
    for i in range(len(arr)):
        product *= arr[i]
    return product

def get_product_of_gcd(arr):
    product = 1
    for i in range(len(arr)):
        product *= get_gcd(arr[i])
    return product

def get_product_of_lcm(arr):
    product = 1
    for i in range(len(arr)):
        product *= get_lcm(arr[i])
    return product

def get_subsets(arr):
    subsets = []
    for i in range(1, len(arr) + 1):
        subsets.extend(get_subsets_of_size(arr, i))
    return subsets

def get_subsets_of_size(arr, size):
    subsets = []
    for i in range(len(arr)):
        if size == 1:
            subsets.append([arr[i]])
        else:
            for j in range(i + 1, len(arr)):
                for k in range(len(subsets)):
                    if len(subsets[k]) == size - 1:
                        subsets.append(subsets[k] + [arr