'''
 pair.
Case 4 : N = 6. Arjuna can make the pair (1,3) and Bhima can not make any more pairs ( without crossing the pair (1,3) )

'''

# Write your code here
import math
for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print("Arjuna")
    elif n%2 == 0:
        print("Arjuna")
    else:
        print("Bhima")