'''


Explanation
Example case 1. The first person only knows about "No" gesture, which is used both in India and abroad. The second person uses "Yes" gesture twice, and "Indian Yes" gesture once. The third person uses "Indian Yes" twice and "No" twice, which makes it impossible to distinguish between Indian and non-Indian.

'''

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        gestures = sys.stdin.readline().strip()
        if 'Y' in gestures:
            print('NOT INDIAN')
        elif 'I' in gestures:
            print('INDIAN')
        else:
            print('NOT SURE')

if __name__ == '__main__':
    main()