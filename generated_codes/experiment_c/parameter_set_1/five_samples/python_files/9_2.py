"""

Note
In the first sample he can make two moves: "CHEFCHEFFFF" -> "CHEFHFFFF" -> "CHEFHFFF" and he cannot make more moves.

In the second sample he can make only one move.

Explanation

Example Test Case 1

Example Test Case 2

Example Test Case 3

Example Test Case 4

Example Test Case 5

Example Test Case 6

Example Test Case 7

Example Test Case 8

Example Test Case 9
"""

s = list(input())

max_moves = 0

while 'C' in s:
    i = s.index('C')
    if s[i+1] == 'H':
        if s[i+2] == 'E':
            if s[i+3] == 'F':
                s[i:i+4] = []
                max_moves += 1
            else:
                break
        else:
            break
    else:
        break

print(max_moves)