'''


Explanation
Example case 1. The first person only knows "No" gesture, which is used in the US. The second person uses "Yes" and "Indian Yes" gestures, which is common in India. The third person uses "Indian Yes", "No" and "Yes" gestures, which could be used by anyone.

'''

import re

def indian_or_not(n,s):
    if re.match(r'^(N|I)+$',s):
        return 'INDIAN'
    elif re.match(r'^(Y|N)+$',s):
        return 'NOT INDIAN'
    else:
        return 'NOT SURE'

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(indian_or_not(n,s))