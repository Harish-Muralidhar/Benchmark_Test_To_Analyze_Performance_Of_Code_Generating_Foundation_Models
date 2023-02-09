"""


"""

import math

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a, a)

def count_occurances(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count

def get_max_and_count(arr, n, g, x, y):
    S = []
    for i in range(x-1, y):
        if gcd(g, arr[i]) > 1:
            S.append(arr[i])
    if len(S) == 0:
        return -1, -1
    else:
        max_element = max(S)
        count = count_occurances(S, len(S), max_element)
        return max_element, count

def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        g, x, y = map(int, input().split())
        max_element, count = get_max_and_count(arr, N, g, x, y)
        print(max_element, count)

if __name__ == '__main__':
    main()