'''

'''

import random

def get_random_array(n):
    return [random.randint(1, n) for i in range(n)]

def get_random_index(n):
    return random.randint(0, n-1)

def get_random_array_a(n):
    array_a = [0] * n
    for i in range(n):
        j = get_random_index(n)
        while j < i:
            j = get_random_index(n)
        for k in range(i, j+1):
            array_a[k] += 1
    return array_a

def get_number_of_different_arrays(n):
    array_b = get_random_array(n)
    number_of_arrays = 0
    for i in range(n):
        array_a = get_random_array_a(n)
        if array_a[i] > array_b[i]:
            number_of_arrays += 1
    return number_of_arrays

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(get_number_of_different_arrays(n))

if __name__ == "__main__":
    main()