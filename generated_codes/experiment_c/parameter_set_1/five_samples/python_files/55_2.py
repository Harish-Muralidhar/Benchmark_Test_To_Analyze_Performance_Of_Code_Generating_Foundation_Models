'''

'''

# Python3 Program to find product of   
# GCD of all subsets of a given set 
  
# function to find GCD of two numbers 
def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# function to find product of GCD of 
# all subsets of a given set 
def findProductOfGcd(arr, n): 
   
    # to store the product of GCD's  
    product = 1; 
  
    # iterating through all the possible subsets 
    for i in range(1, (1 << n)): 
       
        # to store the current subset's GCD 
        currentsubsetGCD = 1; 
       
        # iterating through all the elements of the subset i 
        for j in range(0, n): 
          
            # if the ith bit in the binary representation 
            # of i is set, then the element at index j 
            # is present in the subset i 
            if ((i & (1 << j)) > 0): 
                currentsubsetGCD = gcd(currentsubsetGCD, arr[j]) 
  
        # Updating the product of GCD's 
        product = (product * currentsubsetGCD) % 1000000007
   
    return product 
  
# Driver Code 
n = int(input())
arr = list(map(int, input().split())) 
print(findProductOfGcd(arr, n))