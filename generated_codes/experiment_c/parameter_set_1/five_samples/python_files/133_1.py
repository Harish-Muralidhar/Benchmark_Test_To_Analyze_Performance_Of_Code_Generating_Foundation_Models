'''
 pairs.
Case 4 : N = 6. Arjuna can make the pair (1,3) and Bhima has no choice but to make the pair (2,4). Now, Arjuna can make the pair (5,6) and win. 

For more clarity, see the images in the sample test case.
'''

import math

def calculate_winner(n):
    if n==2:
        return 'Arjuna'
    if n%2==0:
        return 'Arjuna'
    else:
        if n%4 == 3:
            return 'Arjuna'
        else:
            return 'Bhima'

def main():
    result = []
    T = int(input())
    for i in range(T):
        result.append(calculate_winner(int(input())))

    for results in result:
        print(results)

if __name__=="__main__":
    main()