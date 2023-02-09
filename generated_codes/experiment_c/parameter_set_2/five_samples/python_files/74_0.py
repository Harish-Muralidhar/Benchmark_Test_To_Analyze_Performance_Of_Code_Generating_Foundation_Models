'''

Explanation

In the first test case, the only such progression is (2, 4, 6).
In the second test case, there are no such progressions.
In the third test case, the first two terms of the 12^th such progression are 5 and 14.

'''

# Write your code here

def get_longest_progression(L, R, k, n):
    if n == 0:
        return 0, 0
    if L + k > R:
        return 0, 0
    length = 1
    while L + length * k <= R:
        length += 1
    if n > length * (length + 1) // 2:
        return 0, 0
    if n <= length:
        return length, L + (n - 1) * k
    n -= length
    length -= 1
    while n > length:
        n -= length
        length -= 1
    return length + 1, L + (n - 1) * k

T = int(input())

for _ in range(T):
    L, R, k, n = map(int, input().split())
    length, first_term = get_longest_progression(L, R, k, n)
    print(length, first_term)