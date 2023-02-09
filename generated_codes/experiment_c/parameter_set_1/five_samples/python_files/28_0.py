'''

'''

import sys

def main():
    T = int(sys.stdin.readline())
    res = []
    for i in range(T):
        c = sys.stdin.readline().strip()
        if c == 'B' or c == 'b':
            res.append('BattleShip')
        elif c == 'C' or c == 'c':
            res.append('Cruiser')
        elif c == 'D' or c == 'd':
            res.append('Destroyer')
        elif c == 'F' or c == 'f':
            res.append('Frigate')
        else:
            res.append('Error')
    for ele in res:
        print(ele)

if __name__ == '__main__':
    main()