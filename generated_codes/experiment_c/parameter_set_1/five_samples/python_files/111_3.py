'''


'''



# Write your code here

import re


def find_max(input):
    if not re.search('[A-Z]',input):
        return int(input)
    else:
        ind = input.index('A')
        return max(int(input[:ind]+'9'+input[ind+1:]),int(input[:ind]+'1'+input[ind+1:]))

if __name__ == '__main__':
    input = input()
    print(find_max(input))