"""


"""

import sys
import math

def main():
    T = int(input())
    for i in range(T):
        A,B = input().strip().split(' ')
        A,B = int(A),int(B)
        count = 0
        if A == B:
            print(count)
        else:
            while A!=B:
                if A%2 == 0:
                    A = A/2
                else:
                    A = (A-1)/2
                count += 1
            print(count)

if __name__ == '__main__':
    main()