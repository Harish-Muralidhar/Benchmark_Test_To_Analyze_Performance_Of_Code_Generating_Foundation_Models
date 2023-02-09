'''

'''

import math

def is_valid_triangle(a, b, c):
    if a + b + c == 180:
        return True
    else:
        return False

def main():
    t = int(input())
    for i in range(t):
        a, b, c = [int(i) for i in input().split()]
        if is_valid_triangle(a, b, c):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()