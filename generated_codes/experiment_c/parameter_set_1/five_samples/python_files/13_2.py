"""

Explanation

In the first case, all three are already close enough to communicate without any intermediate transceiver.

In the second case, the sous-chef can act as an intermediate transceiver so that all three are able to communicate.

In the third case, no two are close enough to communicate directly, but the Chef and the sous-chef are close enough so that the Chef can use the sous-chef as an intermediate transceiver to talk to the head server. However, the sous-chef and head server are too far apart to be able to communicate directly.

Solution:

"""

import math
for _ in range(int(input())):
    r = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    d1 = math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))
    d2 = math.sqrt(((x1 - x3)**2 + (y1 - y3)**2))
    d3 = math.sqrt(((x2 - x3)**2 + (y2 - y3)**2))
    if d1 <= r or d2 <= r or d3 <= r:
        print('yes')
    else:
        print('no')