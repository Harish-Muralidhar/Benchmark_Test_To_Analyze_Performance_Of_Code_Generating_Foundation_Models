'''

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