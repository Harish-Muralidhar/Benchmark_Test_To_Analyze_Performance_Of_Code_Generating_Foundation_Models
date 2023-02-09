'''

'''

# Solution

import itertools

def check_palindrome(s):
    return s == s[::-1]

def min_deletion(arr):
    n = len(arr)
    min_deletion = n
    for i in range(n):
        for j in range(i+1, n):
            if check_palindrome(arr[i] + arr[j]):
                min_deletion = min(min_deletion, n - 2)
            if check_palindrome(arr[j] + arr[i]):
                min_deletion = min(min_deletion, n - 2)
    return min_deletion

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        print(min_deletion(arr))