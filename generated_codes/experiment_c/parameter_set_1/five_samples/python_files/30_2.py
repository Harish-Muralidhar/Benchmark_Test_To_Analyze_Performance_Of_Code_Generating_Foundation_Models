'''

Explanation

Input : A = 30, B = 40, C = 110
Output : NO
Explanation : A triangle is valid if sum of all 
angles is 180, but here sum of angles is 
30 + 40 + 110 = 180.

Input : A = 45, B = 45, C = 90
Output : YES
Explanation : A triangle is valid if sum of all 
angles is 180, and here sum of angles is 
45 + 45 + 90 = 180

Input : A = 180, B = 0, C = 0
Output : NO
Explanation : A triangle is valid if sum of all 
angles is 180, but here sum of angles is 
180 + 0 + 0 = 180.

'''

import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a,b,c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        if a+b+c == 180:
            print("YES")
        else:
            print("NO")