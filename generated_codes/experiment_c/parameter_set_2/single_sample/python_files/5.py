'''

Explanation

In the first case the sequence contains the favourite sequence as a substring.
In the second case the sequence does not contain the favourite sequence as a substring.

'''

import itertools

def check_substring(n,f):
    if f in n:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n_len = int(input())
        n = input().split()
        f_len = int(input())
        f = input().split()
        print(check_substring(n,f))