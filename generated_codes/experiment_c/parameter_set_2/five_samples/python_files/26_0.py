'''

'''

import sys

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        if N < 10:
            print("What an obedient servant you are!")
        else:
            print("-1")

if __name__ == "__main__":
    main()