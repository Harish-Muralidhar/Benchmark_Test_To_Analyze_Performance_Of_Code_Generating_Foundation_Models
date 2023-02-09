'''

Explanation

Example case 1. The only such progression is (2, 4, 6).

Example case 2. There are two such progressions: (2, 4, 6) and (3, 5, 7).

Example case 3. The first two terms of the 12^th such progression are 5 and 14.

'''

# Write your code here
import math

def find_progression(L, R, k, n):
    if k > R - L:
        return 0, 0
    else:
        count = 0
        for i in range(L, R - k + 1):
            count += math.ceil((R - i) / k)
        if count < n:
            return 0, 0
        else:
            count = 0
            for i in range(L, R - k + 1):
                count += math.ceil((R - i) / k)
                if count >= n:
                    return math.ceil((R - i) / k), i

T = int(input())
for i in range(T):
    L, R, k, n = map(int, input().split())
    length, first_term = find_progression(L, R, k, n)
    print(length, first_term, first_term + k)