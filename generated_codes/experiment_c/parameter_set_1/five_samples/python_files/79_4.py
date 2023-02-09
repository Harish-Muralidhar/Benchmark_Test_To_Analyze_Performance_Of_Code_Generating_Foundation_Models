"""


Explanation:

The trap can be dropped in four places: Down and to the right, down, down and to the left, and to the left.

Dropping the trap down and to the right, it covers the tiles (1,1), (1,2), (2,1), (2,2). Out of these tiles, the tile (1,1) has the least number of bugs, 0.

Dropping the trap down, it covers the tiles (1,1), (1,2), (2,1), (2,2), (3,1), (3,2). Out of these tiles, the tile (1,1) has the least number of bugs, 0.

Dropping the trap down and to the left, it covers the tiles (1,1), (1,2), (2,1), (2,2), (3,1), (3,2), (3,3). Out of these tiles, the tile (1,1) has the least number of bugs, 0.

Dropping the trap to the left, it covers the tiles (1,1), (1,2), (1,3), (2,1), (2,2), (2,3). Out of these tiles, the tile (1,1) has the least number of bugs, 0.

Note that the example output of the given input is:
0 0 0
0 0 0
0 0 0

which is obviously wrong.

"""

import numpy as np
import pandas as pd

def main():
    n, k = map(int, input().split())
    a = np.array([list(map(int, input().split())) for i in range(n)])
    df = pd.DataFrame(a)
    res = []
    for i in range(n-k+1):
        temp = []
        for j in range(n-k+1):
            temp.append(df.iloc[i:i+k, j:j+k].min().min())
        res.append(temp)
    print(res)

if __name__ == '__main__':
    main()