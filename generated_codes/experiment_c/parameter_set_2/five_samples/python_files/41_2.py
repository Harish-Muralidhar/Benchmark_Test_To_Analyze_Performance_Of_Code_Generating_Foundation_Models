'''


'''

# Write your code here

def withdraw(x,y):
    if x%5==0 and x<=y:
        return y-x-0.5
    else:
        return y

x = int(input())
y = float(input())
print('{:.2f}'.format(withdraw(x,y)))