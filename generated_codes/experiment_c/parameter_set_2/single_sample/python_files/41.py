"""


"""

#code

withdraw, balance = input().split()
withdraw = int(withdraw)
balance = float(balance)

if withdraw % 5 == 0 and withdraw <= balance - 0.5:
    balance = balance - withdraw - 0.5

print('%.2f' % balance)