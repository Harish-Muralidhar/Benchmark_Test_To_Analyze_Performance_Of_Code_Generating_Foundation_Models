"""


Explanation
    First case is equivalent to the binary number 11011. 
    Second case is equivalent to the binary number 1. 

"""

import sys

def get_binary(s):
    flag = 1
    binary = ""
    for i in range(len(s)):
        if s[i] == '0':
            if flag == 1:
                binary += '1'
            else:
                binary += '0'
        elif s[i] == '1':
            if flag == 1:
                binary += '0'
            else:
                binary += '1'
        elif s[i] == '2':
            if flag == 1:
                binary += '10'
            else:
                binary += '01'
        elif s[i] == '3':
            if flag == 1:
                binary += '11'
            else:
                binary += '00'
        elif s[i] == '4':
            if flag == 1:
                binary += '100'
            else:
                binary += '001'
        elif s[i] == '5':
            if flag == 1:
                binary += '101'
            else:
                binary += '010'
        elif s[i] == '6':
            if flag == 1:
                binary += '110'
            else:
                binary += '011'
        elif s[i] == '7':
            if flag == 1:
                binary += '111'
            else:
                binary += '000'
        elif s[i] == '8':
            if flag == 1:
                binary += '1000'
            else:
                binary += '0001'
        elif s[i] == '9':
            if flag == 1:
                binary += '1001'
            else:
                binary += '0010'
        elif s[i] == 'A':
            if flag == 1:
                binary += '1010'
            else:
                binary += '0011'
        elif s[i] == 'B':
            if flag == 1:
               