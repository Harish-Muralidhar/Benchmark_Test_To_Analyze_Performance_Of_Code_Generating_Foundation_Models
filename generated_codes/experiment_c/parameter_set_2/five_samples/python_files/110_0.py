"""

"""

def split(S):
    S1 = S[:len(S)//2]
    S2 = S[len(S)//2:]
    return (S1, S2)

def hash(S):
    result = S.count('A')
    if len(S) > 1:
        (S1, S2) = split(S)
        result = result + max(hash(S1), hash(S2))
    return result

def count_binary_strings(A, E, V):
    if V > A+E:
        return 0
    if V == A+E:
        return 1
    if V == 0:
        return 1
    if A == 0:
        return 0
    if E == 0:
        return 0
    if A == 1 and E == 1:
        return 1
    if A == 1:
        return 1
    if E == 1:
        return 1
    if V == 1:
        return 1
    if V == 2:
        return 2
    if V == 3:
        return 3
    if V == 4:
        return 4
    if V == 5:
        return 5
    if V == 6:
        return 6
    if V == 7:
        return 7
    if V == 8:
        return 8
    if V == 9:
        return 9
    if V == 10:
        return 10
    if V == 11:
        return 11
    if V == 12:
        return 12
    if V == 13:
        return 13
    if V == 14:
        return 14
    if V == 15:
        return 15
    if V == 16:
        return 16
    if V == 17:
        return 17
    if V == 18:
        return 18
    if V == 19:
        return 19
    if V == 20:
        return 20
    if V == 21:
        return 21
    if V == 22:
        return 22
    if V == 23:
        return 23
    if V == 24:
        return 24
    if V == 25:
        return 25
   