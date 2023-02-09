'''

Example case 2.
Is it possible to make N equal pieces?
No, no matter how you cut the cake, you can't make 7 equal pieces.
Is it possible to make N pieces?
Yes, you can cut 7 pieces with angles 1, 2, 3, ..., 7.
Is it possible to make N pieces, such that no two of them are equal?
Yes, you can cut 7 pieces with angles 1, 2, 3, ..., 7.

'''
def is_possible_equal_pieces(N):
    if N == 0:
        return True
    if N % 2 == 0:
        return False
    for i in range(1, N):
        if 360 % i == 0 and 360 // i >= N:
            return True
    return False

def is_possible_pieces(N):
    if N == 0:
        return True
    if N == 1:
        return False
    if N % 2 == 0:
        return True
    if N % 3 == 0:
        return True
    for i in range(1, N):
        if 360 % i == 0 and 360 // i >= N:
            return True
    return False

def is_possible_non_equal_pieces(N):
    if N == 0:
        return True
    if N == 1:
        return False
    if N == 2:
        return False
    if N % 2 == 0:
        return False
    if N % 3 == 0:
        return False
    for i in range(1, N):
        if 360 % i == 0 and 360 // i >= N:
            return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    if is_possible_equal_pieces(N):
        print('y', end = ' ')
    else:
        print('n', end = ' ')
    if is_possible_pieces(N):
        print('y', end = ' ')
    else:
        print('n', end = ' ')
    if is_possible_non_equal_pieces(N):
        print('y', end = ' ')
    else:
        print('n', end = ' ')
    print()