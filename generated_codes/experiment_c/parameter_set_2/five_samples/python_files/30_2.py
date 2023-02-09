'''

Explanation:

In the above test case, the sum of the three angles is 180 degress hence the triangle is valid.

In the second test case, the sum of the three angles is 180 degress hence the triangle is valid.

In the third test case, the sum of the three angles is 180 degress hence the triangle is not valid.

'''

import math

def is_valid_triangle(a,b,c):
    if a+b+c == 180:
        return True
    else:
        return False

def main():
    T = int(input())
    for i in range(T):
        a,b,c = map(int,input().split())
        if is_valid_triangle(a,b,c):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()