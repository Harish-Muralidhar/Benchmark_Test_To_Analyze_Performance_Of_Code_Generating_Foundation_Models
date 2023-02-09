/*
*/

import math

def match_pattern(pattern, input_string):
    for i in range(len(pattern)):
        if pattern[i] != '*' and pattern[i] != input_string[i]:
            return False
    return True
    
    
def find_pattern(pattern, input_string, output_string):
    pos = 0
    while pos < len(input_string):
        try:
            pos = input_string.index(pattern, pos)
            output_string = output_string[:pos] + pattern + output_string[pos+len(pattern):]
            pos += len(pattern)
        except:
            break
    return output_string

#print(find_pattern('e', 'chefchef', '*'*8))
#print(find_pattern('chef', 'chefchef', '*'*8))

def find_message(S, message):
    if len(S) == 1:
        return message
    else:
        mid = len(S)//2
        left_half = S[:mid]
        right_half = S[mid:]
        left_string = find_message(left_half, message[:mid])
        right_string = find_message(right_half, message[mid:])
        #print(left_string, right_string)
        
        left_string = find_pattern(left_half, right_string, left_string)
        right_string = find_pattern(right_half, left_string, right_string)
        
        #print(left_string, right_string)
        return left_string+right_string

T = int(input())
for _ in range(T):
    k, message = input().split()
    k = int(k)
    S = ''.join(['0' for i in range(k)])
    #print(S, message)
    print(find_message(S, message))