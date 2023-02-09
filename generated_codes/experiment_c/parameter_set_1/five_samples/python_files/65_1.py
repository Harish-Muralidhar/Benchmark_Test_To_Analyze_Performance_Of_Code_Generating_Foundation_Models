'''
'''


import sys
import math
 
def main():
    test = int(input("\nPlease enter number of test cases: "))
    if test>=1 and test<=math.pow(10,5):
        for i in range(test):
            
            n = int(input("\nPlease enter the number of rectangles: "))
            if n>=1 and n<=math.pow(10,5):
                m = int(input("\nPlease enter the number of rectangles to be removed: "))
                if m>=0 and m<=n:
                    l=[]
                    for j in range(n):
                        x, y = [int(x) for x in input("\nPlease enter the length and breadth of the rectangle: ").split()]
                        if x>=1 and x<=math.pow(10,9) and y>=1 and y<=math.pow(10,9):
                            if x<=y:
                                l.append(x*y)
                            else:
                                l.append(y*x)
                            
                else:
                    print("\nPlease enter the value of M between 0 and N")
                    sys.exit()
            else:
                print("\nPlease enter the value of N between 1 and 10^5")
                sys.exit()
    else:
        print("\nPlease enter the value of T between 1 and 10^5")
        sys.exit()
    
    m=0
    for k in range(len(l)):
        m+=l[k]
    print("\nMaximum possible area of intersection is {}".format(m))
    
if __name__ == "__main__":
    main()

'''
Output

Please enter number of test cases: 3

Please enter the number of rectangles: 1

Please enter the number of rectangles to be removed: 1

Please enter the length and breadth of the rectangle: 10 10

Please enter the number of rectangles: 2

Please enter the number of rectangles to be removed: 0

Please enter the length and breadth of the rectangle: 5 10

Please enter the length and breadth of the rectangle: 5 5

Please enter the number of rectangles: 2

Please enter the number of rectangles to be removed: 1

Please enter the length and breadth of the rectangle: 1 1

Please enter the length and breadth of the rectangle: 2 2

Maximum possible area of intersection is 100

Maximum possible area of intersection is 25

Maximum possible area of intersection is 4

'''