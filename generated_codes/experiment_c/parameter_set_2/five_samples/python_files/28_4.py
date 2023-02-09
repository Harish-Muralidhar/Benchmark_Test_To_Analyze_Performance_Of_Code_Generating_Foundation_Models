"""

"""

# Solution

import sys

def ship_class(letter):
    if letter == 'B' or letter == 'b':
        return 'BattleShip'
    elif letter == 'C' or letter == 'c':
        return 'Cruiser'
    elif letter == 'D' or letter == 'd':
        return 'Destroyer'
    elif letter == 'F' or letter == 'f':
        return 'Frigate'
    else:
        return 'Error'

test_cases = int(input())

for i in range(test_cases):
    letter = input()
    print(ship_class(letter))