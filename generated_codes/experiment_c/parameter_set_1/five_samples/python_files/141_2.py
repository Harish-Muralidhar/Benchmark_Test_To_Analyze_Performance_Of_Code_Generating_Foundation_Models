'''


Explanation :
For the first case, the positions are (1,1) and (2,2), (1,2) and (2,1), (1,2) and (2,3), (1,3) and (2,2), (1,3) and (2,4), (1,4) and (2,3), (2,1) and (1,2), (2,1) and (1,3), (2,2) and (1,1), (2,2) and (1,3), (2,3) and (1,2) and (2,3) and (1,4).

Similarly, for the second case, there are 26 ways.

'''
import math

def fact(r):
    if r == 0 or r == 1:
        return 1
    return r * fact(r - 1)

def nCr(n, r):
    return int(fact(n) / (fact(n - r) * fact(r)))

def main():
    test_case = int(input())

    for _ in range(test_case):
        n, m = map(int, input().split())
        print((nCr(n * m, 2) * (n - 1) * (m - 1)) // 2)

if __name__ == '__main__':
    main()