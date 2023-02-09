'''

'''

import sys
import math

def second_largest(a,b,c):
    if( (a > b) and (a > c) and (b > c)):
        return b
    elif( (b > a) and (b > c) and (a > c)):
        return a
    elif( (c > b) and (c > a) and (b > a)):
        return b
    elif( ( c > b) and (c > a) and (a > b)):
        return a
    else:
        return c

def main():
    if(len(sys.argv) > 1):
        print("Function to find second largest of three numbers")
        print("\nUsage: python3 {0}".format(sys.argv[0]))
        exit(0)
    print("\nSecond Largest Number")
    test_cases = int(input("\nEnter the number of test cases: "))
    for i in range(test_cases):
        a,b,c = input("Enter three numbers: ").split()
        print("\nSecond Largest number is {0}".format(second_largest(a,b,c)))

if __name__ == main():
    main()