'''

'''

# Write your code here

def ship_class(a):
    if a == 'B' or a == 'b':
        return 'BattleShip'
    elif a == 'C' or a == 'c':
        return 'Cruiser'
    elif a == 'D' or a == 'd':
        return 'Destroyer'
    elif a == 'F' or a == 'f':
        return 'Frigate'

n = int(input())
for i in range(n):
    a = input()
    print(ship_class(a))