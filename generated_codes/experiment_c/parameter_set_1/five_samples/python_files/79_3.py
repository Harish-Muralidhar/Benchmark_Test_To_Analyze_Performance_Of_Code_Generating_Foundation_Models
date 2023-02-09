'''


Detail

The first character in the input corresponds to the first tile in the output, (0,0) in this case.  The following character, in the first row of the input, corresponds to the second tile in the output, (0,1) in this case.  This pattern continues for the first row of the input, then the second, and so on.  Here is a rough visualization of the input and output for the given example:

Input:
0 1 2 3
4 5 6 7
8 9 0 1
2 3 4 0

Output:
0 1 2
4 0 0
2 0 0

Sample Input

4 2
0 1 2 3
4 5 6 7
8 9 0 1
2 3 4 0

Sample Output

0 1 2
4 0 0
2 0 0

Explanation

The trap can be dropped at four positions: at (0,0), (0,1), (1,0) or (1,1).

At (0,0), the trap covers the following tiles: (0,0), (0,1), (1,0) and (1,1). The number of bugs on these tiles are 0, 1, 4 and 5, respectively. The tile with minimum bugs is (0,0), which has 0 bugs. Therefore, at (0,0), the trap catches 0 bugs.

At (0,1), the trap covers the following tiles: (0,1), (0,2), (1,1) and (1,2). The number of bugs on these tiles are 1, 2, 5 and 6, respectively. The tile with minimum bugs is (0,1), which has 1 bug. Therefore, at (0,1), the trap catches 1 bug.

At (1,0), the trap covers the following tiles: (1,0), (1,1), (2,0) and (2,1). The number of bugs on these tiles are 4, 5, 8 and 9, respectively. The tile with minimum bugs is (1,0), which has 4 bugs. Therefore, at (1,0), the trap catches 4 bugs.

At (1,1), the trap covers the following tiles: (1,1), (1,2), (2,1) and (2,2). The number of bugs on these tiles are 5, 6, 9 and 0, respectively. The tile with minimum bugs is (2,2), which has 0 bugs. Therefore, at (1,1), the trap catches 0 bugs.

Therefore, the number of bugs caught by the trap, in this case, are 0, 1, 4 and 0, at position (0,0), (0,1), (1,0) and (1,1), respectively.

We can arrange these values in the output as,

0 1 2
4 0 0
2 0 0

'''

import numpy as np

def trap_bugs(n,k,grid):
    output = []
    for i in range(n-k+1):
        temp = []
        for j in range(n-k+1):
            temp.append(np.min(grid[i:i+k, j:j+k]))
        output.append(temp)
    return output

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    grid = np.array([list(map(int, input().split())) for _ in range(n)])
    output = trap_bugs(n,k,grid)
    for item in output:
        print(*item)