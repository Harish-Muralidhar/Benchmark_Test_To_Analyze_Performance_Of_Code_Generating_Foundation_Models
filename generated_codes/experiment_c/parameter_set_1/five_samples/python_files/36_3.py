'''
 

Explanation

Example case 1. "piygu" appears as a part of the modern phrase "piygu ezyfo", while "rzotm" does not.

Example case 2. "kssdy", "tjzhy", and "ljzym" does not occur in any of the modern phrases. "kegqz" appears as a part of the modern phrase "kegqz kegqz kegqz vxvyj".
'''

for _ in range(int(input())):
    n,k = map(int, input().split())
    dictionary = input().split()
    for _ in range(k):
        phrase = input().split()[1:]
        for word in phrase:
            if word in dictionary:
                print('YES', end=' ')
                break
        else:
            print('NO', end=' ')
    print()