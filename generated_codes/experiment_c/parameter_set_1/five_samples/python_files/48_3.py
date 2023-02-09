"""

"""

"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here

import numpy as np

def check_missing_doll(n, arr):
    if(n%2 == 1):
        arr = np.array(arr)
        x = np.unique(arr, return_counts=True)
        for i in range(len(x[0])):
            if(x[1][i]%2 == 1):
                return x[0][i]

def main():
    T = int(input())
    while(T):
        N = int(input())
        arr = []
        for i in range(N):
            arr.append(int(input()))
        print(check_missing_doll(N, arr))
        T -= 1

if __name__ == "__main__":
    main()