'''


*/

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Your function should return an integer
def ways(n,m):
    #code here
    #return the number of ways in which knights can be placed
    return((n*m-1)*(n*m-2)/2-n*m*(n*m-1)/2)
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        nm=[int(x) for x in input().strip().split()]
        n=nm[0]
        m=nm[1]
        
        print(math.floor(ways(n,m)))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends