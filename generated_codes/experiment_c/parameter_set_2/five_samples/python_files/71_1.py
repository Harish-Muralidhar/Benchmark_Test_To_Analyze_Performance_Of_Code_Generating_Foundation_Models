'''

'''

import random

def get_random_array(n):
    return [random.randint(1, n) for _ in range(n)]

def get_random_index(n):
    return random.randint(0, n-1)

def get_random_index_greater_than(n, i):
    return random.randint(i, n-1)

def increment_array(a, i, j):
    for k in range(i, j+1):
        a[k] += 1

def is_array_valid(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

def get_valid_arrays(n):
    b = get_random_array(n)
    a = [0] * n
    while True:
        i = get_random_index(n)
        j = get_random_index_greater_than(n, i)
        increment_array(a, i, j)
        if is_array_valid(a, b):
            return a

def get_number_of_valid_arrays(n):
    count = 0
    while True:
        a = get_valid_arrays(n)
        count += 1
        if a == [n] * n:
            break
    return count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_number_of_valid_arrays(n))

if __name__ == '__main__':
    main()