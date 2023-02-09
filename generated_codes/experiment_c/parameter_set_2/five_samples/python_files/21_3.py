'''

Explanation

In the first test case, 1 divided by 2 has a remainder 1.
In the second test case, remainder when 100 is divided by 200 is 100.
In the third test case, remainder when 10 is divided by 40 is 10.

'''

import sys

def remainder(a,b):
    return a%b

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = remainder(a, b)
        print(result)