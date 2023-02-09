"""
Example case 2. In the first turn Sasha will choose 2, while Chef will choose 3. Since 2^3 < 3^2 girl will not kiss boy. In the second turn girl will choose 1, while boy will choose 4. Since 1^4 > 4^1 girl will kiss boy. Hence answer is 1 + 0.5 = 1.5.
Example case 3. In the first turn Sasha will choose 4, while Chef will choose 2. Since 4^2 < 2^4 girl will not kiss boy. In the second turn girl will choose 2, while boy will choose 2. Since 2^2 = 2^2 girl will not kiss boy. Hence answer is 0

"""

from random import randrange
from math import log as ln

def answer(x,y):
    
    if y==0:
        return x
    return answer(y,x%y)
    
if __name__=="__main__":
    t=int(input())
    while t>0:
        n=int(input())
        sasha=[int(i) for i in input().split()]
        chef=[int(i) for i in input().split()]
        count=0.0
        for i in range(n):
            x=chef[randrange(len(chef))]
            y=sasha[randrange(len(sasha))]
            if x!=0 and y!=0:
                gcd=answer(x,y)
                if (ln(x)/ln(gcd))>=(ln(y)/ln(gcd)):
                    count+=1.0
            else:
                if x==0:
                    x=1
                if y==0:
                    y=1
                if (ln(x)/ln(y))>=(ln(y)/ln(x)):
                    count+=1.0
            chef.remove(x)
            sasha.remove(y)
        print("{0:.6f}".format(count))
        t-=1