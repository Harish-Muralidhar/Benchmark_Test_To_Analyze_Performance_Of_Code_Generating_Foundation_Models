'''

'''

import sys

def remainder(a,b):
    return a%b

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a,b = map(int, input().split())
        print(remainder(a,b))