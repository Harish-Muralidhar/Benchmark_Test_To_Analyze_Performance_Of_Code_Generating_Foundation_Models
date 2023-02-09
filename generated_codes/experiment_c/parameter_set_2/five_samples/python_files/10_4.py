'''

Explanation
The optimal way is to move from 1-st to 2-nd street, then from 2-nd to 4-th street and then from 4-th to 3-rd street. The product of the special numbers of the visited streets equals to 1 * 2 * 4 * 3 = 24, but it is not minimal. The minimal product is 1 * 2 * 4 * 3 / 2 = 8.

'''

import sys

def min_product(n, k, a):
    # return the minimal product of all the visited streets' special numbers
    return 1

if __name__ == "__main__":
    # For fast I/O
    inp = sys.stdin.read().splitlines()
    #print(inp)
    #sys.stdout = open("file.txt", "w")
    #sys.stdout = sys.__stdout__
    n, k = map(int, inp[0].split())
    a = list(map(int, inp[1].split()))
    print(min_product(n, k, a))