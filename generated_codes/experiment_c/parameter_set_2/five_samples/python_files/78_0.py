"""


Explanation

In the example test case, the enemy battleship is located at the Y coordinate 2. It has three guns, located at (-2, 2), (-1, 2), and (1, 2).

The supernatural rocks are located at (-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1), and (2, 0).

The line connecting your cannon and (-2, 2) does not go through any rocks, so you can destroy that gun.

The line connecting your cannon and (-1, 2) goes through the rock at (-1, 1), so you cannot destroy that gun.

The line connecting your cannon and (1, 2) goes through the rock at (1, 1), so you cannot destroy that gun.

You can destroy exactly two guns, so the answer is 2.

"""

import math

def main():
    t = int(input())
    while t > 0:
        y, x1, x2 = map(int, input().split())
        x1 = abs(x1)
        x2 = abs(x2)
        count = 0
        for i in range(x1, x2+1):
            if not math.gcd(i, y) == 1:
                count += 1
        print(count)
        t -= 1

if __name__ == '__main__':
    main()