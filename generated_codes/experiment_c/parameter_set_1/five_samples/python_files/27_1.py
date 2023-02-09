'''
'''

import sys

def totalExpenses(quantity, price):
    if quantity > 1000:
        return quantity*price*0.90
    else:
        return quantity*price
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        quantity, price = input().split()
        quantity = int(quantity)
        price = int(price)
        print(totalExpenses(quantity, price))