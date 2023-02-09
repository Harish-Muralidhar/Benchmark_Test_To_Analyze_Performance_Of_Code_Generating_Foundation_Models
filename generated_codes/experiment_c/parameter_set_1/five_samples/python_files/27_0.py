"""


https://practice.geeksforgeeks.org/problems/discounts/0
"""
import sys

def get_discount(quantity, price):
    if quantity <= 1000:
        return price * quantity
    return quantity * price * 0.9

def discounts():
    t = int(input())
    while t > 0:
        line = input().strip()
        quantity = int(line.split(' ')[0])
        price = int(line.split(' ')[1])
        print(get_discount(quantity, price))
        t -= 1

if __name__ == '__main__':
    discounts()