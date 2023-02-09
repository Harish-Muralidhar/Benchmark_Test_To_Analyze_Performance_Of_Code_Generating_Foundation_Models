'''


Explanation
Example case 1. The first person only knows about "No" gesture, which is used both in India and abroad. The second person uses "Yes" gesture twice and "Indian Yes" gesture once. The third person uses "Indian Yes" twice and "No" gesture once. Hence the second person is from India and the third is not from India. The first person could be from either country.

'''

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    if S.count('Y') > 0 and S.count('I') == 0:
        print('NOT INDIAN')
    elif S.count('I') > 0:
        print('INDIAN')
    else:
        print('NOT SURE')