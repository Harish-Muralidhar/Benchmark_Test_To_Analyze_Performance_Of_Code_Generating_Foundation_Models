'''
 pair ( without crossing Bhima's pair ).
Case 4 : N = 6. Arjuna can make the pair (1,4) and Bhima can not make any more pairs ( without crossing the pair (1,4) )
'''

# cook your dish here
for _ in range(int(input())):
    n=int(input())
    print("Arjuna" if n%3 else "Bhima")