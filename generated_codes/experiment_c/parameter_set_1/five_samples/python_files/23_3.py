'''



'''

import sys

def minimumNotes(N):
    if N<=0:
        return 0
    count =0
    for i in [100,50,10,5,2,1]:
        count+=N/i
        N = N%i
        if N==0:
            return count

if __name__=="__main__":
    T=input()
    for i in range(T):
        N=input()
        print minimumNotes(N)