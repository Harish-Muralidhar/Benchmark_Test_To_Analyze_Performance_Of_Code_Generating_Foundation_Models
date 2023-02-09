'''

Explanation

In the first test case the sequence contains the favourite sequence as a substring.

In the second test case the sequence doesn't contain the favourite sequence as a substring.

'''

import re

def check_substring(n,f):
    if re.search(f,n):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n_len = int(input())
        n = input()
        f_len = int(input())
        f = input()
        print(check_substring(n,f))