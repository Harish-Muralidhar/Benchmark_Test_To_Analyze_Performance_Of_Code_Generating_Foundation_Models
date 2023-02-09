'''

'''

import sys

f = open(sys.argv[1], 'r')

test_cases = f.read().splitlines()

for test in test_cases:
    if test == 'B' or test == 'b':
        print('BattleShip')
    elif test == 'C' or test == 'c':
        print('Cruiser')
    elif test == 'D' or test == 'd':
        print('Destroyer')
    elif test == 'F' or test == 'f':
        print('Frigate')