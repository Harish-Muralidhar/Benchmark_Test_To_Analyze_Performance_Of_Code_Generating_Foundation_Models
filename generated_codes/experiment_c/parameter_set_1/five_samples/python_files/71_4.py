"""

"""

import random


def get_rand_array(n):
    return [random.randint(1, n) for i in range(n)]


def get_rand_index(n):
    return random.randint(0, n)


def get_rand_range_index(n):
    low = random.randint(0, n)
    high = random.randint(low, n)
    return low, high


def get_count(n, b):
    count = 0
    for _ in range(100):
        a = [0 for i in range(n)]
        for _ in range(n):
            i, j = get_rand_range_index(n)
            for k in range(i, j + 1):
                a[k] += 1

        if all(a[i] <= b[i] for i in range(n)):
            count += 1
    return count


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = [int(i) for i in input().strip().split()]
        count = get_count(n, b)
        print(count)


if __name__ == '__main__':
    main()