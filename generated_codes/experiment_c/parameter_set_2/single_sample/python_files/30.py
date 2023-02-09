'''

'''

import math

def isValidTriangle(a,b,c):
    if (a+b+c==180):
        return True
    else:
        return False

def main():
    print("Enter the number of test cases: ")
    T = int(input())
    for i in range(T):
        print("Enter the three angles of the triangle: ")
        a,b,c = map(int, input().split())
        if(isValidTriangle(a,b,c)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()