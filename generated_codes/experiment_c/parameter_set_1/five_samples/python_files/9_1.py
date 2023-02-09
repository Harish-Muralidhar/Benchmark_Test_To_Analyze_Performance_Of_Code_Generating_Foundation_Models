'''

Sample Explanation

In the first example, Chef can make two moves: he can erase the symbols from 2-nd to 4-th positions (thus obtaining the string "CHHFF"), and then he can erase the symbols from 5-th to 7-th positions (obtaining the string "CHH"). Note that the string "CHH" is a result of the game and it doesn't contain the word "CHEF".

In the second example, Chef can make only one move: erasing the symbols from 5-th to 7-th positions (so, he obtain the string "CHHEEEFC").

'''
import numpy as np
def chess_game(s):
    s = s.replace('C', ' ')
    s = s.replace('H', ' ')
    s = s.replace('E', ' ')
    s = s.replace('F', ' ')
    print(s)
    s = s.split()
    count = 0
    for i in range(len(s)):
        if s[i] == 'chef':
            count = count + 1
    return count
s = 'CHHEEEFCCH'
print(chess_game(s))

#s = input().split()
#print(s)
#s = s.replace('C', ' ')
#print(s)