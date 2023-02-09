'''


Question Answer

a=int(input("enter the amount of money to withdraw"))
b=float(input("enter the account balance"))
if(a%5==0):
    if(a+0.50<b):
        print(b-a-0.50)
    else:
        print(b)
else:
    print(b)

'''

# Question 3
# Create a python program to guess a randomly generated number.


# Question Answer

'''

import random

a=random.randint(1,9)
b=int(input("guess the number between 1 to 9"))
if(a==b):
    print("you won")
else:
    print("you loose")
    print("the number was",a)

'''

# Question 4
# Write a python code to create a list of the even numbers from 0 to 20.

# Question Answer


a=[i for i in range(0,21) if i%2==0]
print(a)