'''
 pairs.
Case 4 : N = 6. Arjuna makes the pair (1,3). Bhima can not make any more pairs ( without crossing the pair (1,3) )

'''

# Write your code here

def game(n):
    if n%2==0:
        return "Arjuna"
    else:
        return "Bhima"

t=int(input())
for i in range(t):
    n=int(input())
    print(game(n))