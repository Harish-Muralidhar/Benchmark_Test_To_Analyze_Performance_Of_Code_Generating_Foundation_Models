"""

"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def get_prime_cross_count(arr, row, col):
    left = 0
    right = 0
    top = 0
    bottom = 0
    for i in range(col-1, -1, -1):
        if arr[row][i] == '#':
            break
        left += 1
    for i in range(col+1, len(arr[0])):
        if arr[row][i] == '#':
            break
        right += 1
    for i in range(row-1, -1, -1):
        if arr[i][col] == '#':
            break
        top += 1
    for i in range(row+1, len(arr)):
        if arr[i][col] == '#':
            break
        bottom += 1
    min_val = min(left, right, top, bottom)
    if is_prime(min_val):
        return 1
    return 0

def get_prime_cross_count_of_map(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '#':
                continue
            count += get_prime_cross_count(arr, i, j)
    return count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        row, col = map(int, input().split())
        arr = []
        for j in range(row):
            arr.append(list(input()))
        print(get_prime_cross_count_of_map(arr))