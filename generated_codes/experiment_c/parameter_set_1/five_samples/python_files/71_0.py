"""

"""

import numpy as np
import random

#Main Function
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = np.array([int(x) for x in input().split()])
        a = np.zeros(n)
        for i in range(n):
            j = random.randint(i,n-1)
            for k in range(i,j+1):
                a[k]+=1
        print(sum(a>b))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Executing main()
if __name__ == "__main__":
    main()