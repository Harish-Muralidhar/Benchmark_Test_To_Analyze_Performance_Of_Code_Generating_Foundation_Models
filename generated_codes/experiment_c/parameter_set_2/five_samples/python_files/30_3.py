'''

Explanation:

In the above test case, the sum of the three angles is 180 degress hence the triangle is valid.

In the second test case, the sum of the three angles is 180 degress hence the triangle is valid.

In the third test case, the sum of the three angles is 180 degress hence the triangle is not valid.

'''

# Write your code here
import math

def is_valid_triangle(a,b,c):
    if a+b+c != 180:
        return False
    else:
        return True

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a,b,c = map(int, input().split())
        print('YES' if is_valid_triangle(a,b,c) else 'NO')