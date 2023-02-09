"""

Solution

"""


import math

def count_similar_paths(n, u, v):
    """
    Counts the number of pairs (w, t)
    such the path from w to t is the same
    as the path from u to v.
    """
    if not (1 <= u <= n and 1 <= v <= n):
        return 0
    # Find the largest element e in the path from u to v.
    e = max(u, v)
    # Find the smallest power of 2 that is greater
    # than or equal to e.
    p = int(math.ceil(math.log(e, 2)))
    # Calculate the number of pairs (w, t) such that
    # w and t are smaller than or equal to 2**p.
    return (2**(p+1)) - 1

# Test your code against the following inputs:
print(count_similar_paths(10, 2, 2))
print(count_similar_paths(10, 2, 6))
print(count_similar_paths(11, 9, 11))
print(count_similar_paths(8, 1, 8))
print(count_similar_paths(8, 8, 1))