'''


'''

import math

def main():
    T = int(input())
    for i in range(T):
        A, B = map(int, input().split())
        print(int(math.log2(B/A)))

if __name__ == '__main__':
    main()