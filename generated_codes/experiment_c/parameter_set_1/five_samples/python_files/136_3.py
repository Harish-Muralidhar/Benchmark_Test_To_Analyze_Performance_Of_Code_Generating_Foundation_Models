"""


"""

def mod(n) : 
    return n % (10**9 + 7) 
  

def compute(n, k) : 
  
    # Base case 
    if n == 0 : 
        return 1
  
    # Recursive case. First, calculate 
    # the value of compute(n-1, k). 
    ans = compute(n - 1, k) 
  
    # Value of compute(n, k) is 
    # sum of compute(n-1, k) and 
    # compute(n-1, k-1) 
    ans = mod(ans + compute(n - 1, k - 1)) 
  
    return mod(ans) 
  

def numberOfWays(n, k) : 
    return mod(compute(n, k)) 


t = int(input())

for i in range(t):
    n,k = map(int,input().split())

    print(numberOfWays(n,k))