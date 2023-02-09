'''

'''

import math

T = int(input())

for i in range(T):
    Qty,Pr = input().split()
    Qty = int(Qty)
    Pr = int(Pr)

    Exp = Qty*Pr
    if Qty > 1000:
        Exp = Exp - (Exp*0.1)
    
    print(Exp)