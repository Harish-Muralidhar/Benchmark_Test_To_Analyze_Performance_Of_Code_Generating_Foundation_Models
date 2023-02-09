'''

'''

# Write your code here
import math

def split(S):
    if len(S) == 1:
        return (S, "")
    else:
        return (S[0:math.ceil(len(S)/2)], S[math.ceil(len(S)/2):])

def hash(S):
    result = S.count('A')
    if len(S) > 1:
        (S1, S2) = split(S)
        result = result + max(hash(S1), hash(S2))
    return result

def count(A, E, V):
    if V == 0:
        return 1
    if A == 0:
        if E == 0:
            return 0
        else:
            return count(A, E-1, V-1)
    if E == 0:
        return count(A-1, E, V-1)
    return count(A-1, E, V-1) + count(A, E-1, V-1)

T = int(input())
for i in range(T):
    A, E, V = map(int, input().split())
    print(count(A, E, V))