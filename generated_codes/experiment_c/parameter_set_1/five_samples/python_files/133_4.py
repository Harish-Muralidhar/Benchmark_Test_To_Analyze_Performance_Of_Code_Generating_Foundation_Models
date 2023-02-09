'''
 pair without crossing Bhima's pair. So, Bhima wins the game.
Case 4 : N = 6. Arjuna makes the pair (1,3) first. Bhima can not make further pairs without crossing the pair (1,3). So, Arjuna wins the game.

'''

for _ in range(int(input())):
    n = int(input())
    
    if n%2==0:
        print('Arjuna')
    else:
        print('Bhima')