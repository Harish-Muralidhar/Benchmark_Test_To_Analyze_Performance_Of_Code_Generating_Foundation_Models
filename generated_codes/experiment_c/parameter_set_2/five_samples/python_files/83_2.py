"""

"""

import sys

def read_input():
    n, k, p = map(int, sys.stdin.readline().split())
    seq = [int(sys.stdin.readline()) for _ in range(n)]
    return n, k, p, seq

def min_sum_mod(n, k, p, seq):
    # TODO: implement this function
    return 0

def main():
    n, k, p, seq = read_input()
    print(min_sum_mod(n, k, p, seq))

if __name__ == '__main__':
    main()