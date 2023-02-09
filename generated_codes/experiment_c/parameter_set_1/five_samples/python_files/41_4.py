'''


===========================================================

'''
#import necessary libraries
import math

x = int(input("Enter the amount to be withdrawn: "))
y = float(input("Enter the initial account balance: "))

if x % 5 == 0 and x <= y:
    z = y - x - 0.5
    print("%.2f" %z)
else:
    print("%.2f" %y)