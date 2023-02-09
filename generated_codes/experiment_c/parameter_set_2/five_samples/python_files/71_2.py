'''

'''

import random

def is_valid(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

def generate_arrays(n):
    b = [random.randint(1, n) for i in range(n)]
    a = [0] * n
    for i in range(n):
        j = random.randint(i, n-1)
        for k in range(i, j+1):
            a[k] += 1
    if is_valid(a, b):
        return a
    else:
        return generate_arrays(n)

def count_possible_arrays(n):
    b = [random.randint(1, n) for i in range(n)]
    count = 0
    for i in range(n):
        j = random.randint(i, n-1)
        for k in range(i, j+1):
            a[k] += 1
    if is_valid(a, b):
        count += 1
    return count

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        b = [int(x) for x in input().split()]
        a = generate_arrays(n)
        print(a)

if __name__ == '__main__':
    main()