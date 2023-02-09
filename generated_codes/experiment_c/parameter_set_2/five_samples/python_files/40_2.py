"""


Explanation
Example case 1. The first person only knows the Indian head-bob, but that's not enough to prove that he is Indian.
Example case 2. The second person uses the Indian head-bob, and also the normal "Yes" gesture. Hence, he is Indian.
Example case 3. The third person only uses the "No" gesture. This is sufficient to prove that he is not Indian.

"""

import sys

def isIndian(gestures):
    if gestures.count('Y') > 0:
        return 'NOT INDIAN'
    elif gestures.count('I') > 0:
        return 'INDIAN'
    else:
        return 'NOT SURE'

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        gestures = sys.stdin.readline().strip()
        print(isIndian(gestures))