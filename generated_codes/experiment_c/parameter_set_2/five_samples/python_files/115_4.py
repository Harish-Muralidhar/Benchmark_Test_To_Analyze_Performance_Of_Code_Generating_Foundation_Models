'''

'''

import sys

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        print(gcd(A))

def gcd(A):
    ans = A[0]
    for i in range(1, len(A)):
        ans = gcd_util(ans, A[i])
    return ans

def gcd_util(a, b):
    if a == b:
        return a
    if a > b:
        return gcd_util(a-b, b)
    return gcd_util(a, b-a)

if __name__ == "__main__":
    main()