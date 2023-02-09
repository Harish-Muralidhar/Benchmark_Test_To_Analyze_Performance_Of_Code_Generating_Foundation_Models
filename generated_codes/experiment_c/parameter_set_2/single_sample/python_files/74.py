"""

Explanation

In the first test case, the only such progression is (2, 4, 6).

In the second test case, there are no such progressions.

In the third test case, the first such progression is (1, 9, 17, 25) and the second is (5, 13, 21, 29).

"""

def get_longest_progression(L, R, k, n):
    if n == 0:
        return 0, 0
    if L == R:
        return 1, L
    if k == 1:
        return R - L + 1, L
    if k == 2:
        return (R - L + 1) // 2 + 1, L
    if k == 3:
        return (R - L + 1) // 3 + 1, L
    if k == 4:
        return (R - L + 1) // 4 + 1, L
    if k == 5:
        return (R - L + 1) // 5 + 1, L
    if k == 6:
        return (R - L + 1) // 6 + 1, L
    if k == 7:
        return (R - L + 1) // 7 + 1, L
    if k == 8:
        return (R - L + 1) // 8 + 1, L
    if k == 9:
        return (R - L + 1) // 9 + 1, L
    if k == 10:
        return (R - L + 1) // 10 + 1, L
    if k == 11:
        return (R - L + 1) // 11 + 1, L
    if k == 12:
        return (R - L + 1) // 12 + 1, L
    if k == 13:
        return (R - L + 1) // 13 + 1, L
    if k == 14:
        return (R - L + 1) // 14 + 1, L
    if k == 15:
        return (R - L + 1) // 15 + 1, L
    if k == 16:
        return (R - L + 1) // 16 + 1, L
    if k == 17:
        return (R - L +