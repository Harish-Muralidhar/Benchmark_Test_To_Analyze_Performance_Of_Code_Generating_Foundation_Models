'''

'''

import sys

def ship_class(c):
    if c == 'B' or c == 'b':
        return 'BattleShip'
    elif c == 'C' or c == 'c':
        return 'Cruiser'
    elif c == 'D' or c == 'd':
        return 'Destroyer'
    elif c == 'F' or c == 'f':
        return 'Frigate'
    else:
        return 'Error'

t = int(input())
for i in range(t):
    c = input()
    print(ship_class(c))