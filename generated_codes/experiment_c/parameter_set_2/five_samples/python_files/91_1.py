'''

Explanation:

The initial configuration is:

0 0 0
1 1 0
1 1 0

The final configuration is:

1 1 1
1 1 1
1 1 1

One way to achieve the final configuration is to press the 0th row button once.

The initial configuration is:

0 0 0
1 1 0
1 1 0

The final configuration is:

1 1 1
1 1 1
1 1 1

One way to achieve the final configuration is to press the 0th row button once.

The initial configuration is:

1 1 1
1 1 0
1 1 0

The final configuration is:

1 1 1
1 1 1
1 1 1

One way to achieve the final configuration is to press the 2nd column button once.

The initial configuration is:

1 1 1
1 1 1
1 1 0

The final configuration is:

1 1 1
1 1 1
1 1 1

One way to achieve the final configuration is to press the 2nd column button once.

The initial configuration is:

1 1 1
1 1 1
1 1 1

The final configuration is:

1 1 1
1 1 1
1 1 1

The initial and the final configurations are the same.

The total number of button presses is 1 + 1 = 2.

The first button press is the 0th row button, and the second button press is the 2nd column button.

The output is:

1
0 
1
2 

'''

import numpy as np

def check_row_col(matrix, row, col):
    if matrix[row][col] == 1:
        return 0
    else:
        return 1

def check_row(matrix, row):
    if matrix[row][0] == 1:
        return 0
    else:
        return 1

def check_col(matrix, col):
    if matrix[0][col] == 1:
        return 0
    else:
        return 1

def check_matrix(matrix):
    for i in range(len(matrix)):
       