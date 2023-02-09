'''


'''

def withdraw_money(x,y):
    if x%5==0 and x<=y:
        return y-x-0.5
    else:
        return y

print(withdraw_money(30,120.00))
print(withdraw_money(42,120.00))
print(withdraw_money(300,120.00))