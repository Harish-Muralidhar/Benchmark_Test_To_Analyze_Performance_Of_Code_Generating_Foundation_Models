'''

Solution:

'''

import math
def main():
    T = int(input())
    while T:
        N = int(input())
        A = list(map(int,input().split()))
        min_val = min(A)
        print(min_val)
        T -= 1

if __name__ == "__main__":
    main()