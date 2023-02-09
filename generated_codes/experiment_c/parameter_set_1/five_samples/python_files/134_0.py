'''

(1, 4, 2, 3) -> (1, 4) -> (4)


(3, 4, 1, 2) -> (3, 4) -> (4)


(4, 2, 1, 3) -> (4, 1) -> (4)


(2, 3, 1, 4) -> (2, 3) -> (3)


(2, 4, 3, 1) -> (2, 4) -> (4)


(3, 1, 4, 2) -> (3, 1) -> (3)


(1, 3, 4, 2) -> (1, 3) -> (3)


(4, 3, 2, 1) -> (4, 3) -> (4)


(2, 1, 4, 3) -> (2, 1) -> (2)


(1, 2, 4, 3) -> (1, 2) -> (2)


(3, 4, 2, 1) -> (3, 4) -> (4)


(1, 4, 3, 2) -> (1, 4) -> (4)


(4, 2, 3, 1) -> (4, 2) -> (4)


(2, 1, 3, 4) -> (2, 1) -> (2)


(1, 3, 2, 4) -> (1, 3) -> (3)


(3, 2, 1, 4) -> (3, 2) -> (3)


(4, 1, 2, 3) -> (4, 1) -> (4)


(2, 3, 4, 1) -> (2, 3) -> (3)


(1, 2, 3, 4) -> (1, 2) -> (2)


(3, 1, 2, 4) -> (3, 1) -> (3)


(2, 4, 1, 3) -> (2, 4) -> (4)

Note

In the first example we have 2^1 = 2 knights, so we have 2 initial configurations: (1, 2) and (2, 1). Both of them lead to the final (1, 2) -> (2) and (2, 1) -> (2), so each participant has 1/2 chances.

In the second example we have 2^2 = 4 knights, so we have 4! = 24 initial configurations. 8 of them lead to the final (2, 4) and (4, 2), so each participant has 1/3 chances.

'''
from math import factorial
def permutations(n):
    return factorial(n)

def permute(n):
    if n == 1:
        return 2
    return permutations(n) * permute(n-1)

def knights(k):
    return permute(2**k)

def chances(k,n):
    return knights(k) // (2**(k)*factorial(n))

def main():
    k,n = map(int, input().split())
    print(chances(k,n))

if __name__ == "__main__":
    main()