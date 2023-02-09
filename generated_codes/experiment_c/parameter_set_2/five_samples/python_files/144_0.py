"""

"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def get_prime_cross_count(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '#':
                continue
            left = 0
            right = 0
            top = 0
            bottom = 0
            for k in range(j - 1, -1, -1):
                if matrix[i][k] == '#':
                    break
                left += 1
            for k in range(j + 1, cols):
                if matrix[i][k] == '#':
                    break
                right += 1
            for k in range(i - 1, -1, -1):
                if matrix[k][j] == '#':
                    break
                top += 1
            for k in range(i + 1, rows):
                if matrix[k][j] == '#':
                    break
                bottom += 1
            if is_prime(min(left, right, top, bottom)):
                count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        r, c = [int(i) for i in input().split()][0:2]
        matrix = []
        for i in range(r):
            matrix.append(input())
        print(get_prime_cross_count(matrix))