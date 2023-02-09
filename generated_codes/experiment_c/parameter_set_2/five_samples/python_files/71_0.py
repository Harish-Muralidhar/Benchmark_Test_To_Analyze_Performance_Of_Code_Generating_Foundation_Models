'''

'''

import random

def generate_array(n):
    return [random.randint(1,n) for i in range(n)]

def generate_array_A(n):
    return [0 for i in range(n)]

def increment_array(A, i, j):
    for k in range(i, j+1):
        A[k] += 1
    return A

def check_validity(A, B):
    for i in range(len(A)):
        if A[i] > B[i]:
            return False
    return True

def generate_random_array(n):
    A = generate_array_A(n)
    B = generate_array(n)
    i = 0
    while i < n:
        j = random.randint(i, n-1)
        A = increment_array(A, i, j)
        if check_validity(A, B):
            i += 1
        else:
            A = generate_array_A(n)
    return A

def generate_all_arrays(n):
    A = generate_array_A(n)
    B = generate_array(n)
    i = 0
    while i < n:
        j = random.randint(i, n-1)
        A = increment_array(A, i, j)
        if check_validity(A, B):
            i += 1
        else:
            A = generate_array_A(n)
    return A

def generate_all_arrays_recursive(n, A, B, i):
    if i == n:
        return A
    j = random.randint(i, n-1)
    A = increment_array(A, i, j)
    if check_validity(A, B):
        return generate_all_arrays_recursive(n, A, B, i+1)
    else:
        return generate_all_arrays_recursive(n, generate_array_A(n), B, i)

def generate_all_arr