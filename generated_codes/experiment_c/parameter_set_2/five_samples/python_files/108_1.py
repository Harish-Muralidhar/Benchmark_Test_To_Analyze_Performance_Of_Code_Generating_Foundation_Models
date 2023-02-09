'''


'''

# Write your code here

import math

def find_min_cards(n):
    if n == 1:
        return 1
    else:
        return math.ceil(math.log2(n)) + 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(find_min_cards(n))