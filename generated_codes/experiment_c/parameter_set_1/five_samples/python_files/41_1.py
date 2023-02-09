"""




@author: user
"""
x=input("enter withdraw amount")
y=input("enter balance")
x=int(x)
y=int(y)
if x%5==0:
    if x<=y:
        
        z=y-x
        z=z-0.5
        z=round(z,2)
        
        print(round(z,2))
    else:
        print(y)
else:
    print(y)