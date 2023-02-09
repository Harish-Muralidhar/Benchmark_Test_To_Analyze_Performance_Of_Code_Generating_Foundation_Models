'''

Example case 2.
Is it possible to make N equal pieces?
No, no matter how you cut the cake, you will be able to make at most 4 equal pieces.
Is it possible to make N pieces?
Yes, you may cut the cake into 7 pieces with angles 87, 87, 87, 87, 88, 88, 89.
Is it possible to make N pieces, such that no two of them are equal?
Yes, you may cut the cake into 7 pieces with angles 87, 87, 87, 87, 88, 88, 89.
'''

for _ in range(int(input())):
    n = int(input())
    if(n>4):
        print('n y y')
    elif(n==4):
        print('y y y')
    elif(n==3):
        print('n y n')
    elif(n==2):
        print('n n n')