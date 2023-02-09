"""

"""

#code 

x = int(input("Enter the amount to be withdrawn:"))
y = float(input("Enter the account balance:"))

if (x % 5) == 0 and (x + 0.5) <= y:
    print("Successful Transaction. Available Balance:",round(y-(x+0.5),2))
else:
    print("Unsuccessful Transaction. Available Balance:",y)