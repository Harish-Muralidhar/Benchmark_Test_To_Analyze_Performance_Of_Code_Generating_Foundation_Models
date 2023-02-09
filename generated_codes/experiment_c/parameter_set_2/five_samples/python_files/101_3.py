"""


"""

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_correct(k, leaf_count):
    if k == 1:
        return leaf_count[0] == 1
    if not is_prime(k):
        return False
    if leaf_count[0] != 1:
        return False
    if leaf_count[k-1] != 2:
        return False
    if k == 2:
        return True
    for i in range(1, k-1):
        if leaf_count[i] != 0:
            return False
    return True

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        k = int(input())
        leaf_count = list(map(int, input().split()))
        if is_correct(k, leaf_count):
            print("Yes")
        else:
            print("No")