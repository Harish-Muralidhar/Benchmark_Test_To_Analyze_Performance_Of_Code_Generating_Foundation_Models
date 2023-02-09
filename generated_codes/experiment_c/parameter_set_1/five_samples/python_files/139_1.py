"""

"""
#code

def isPossible(arr, n, sum1, sum2): 
      
    # If we have reached last index.  
    # Compare sum of elements at current  
    # index in both arrays 
    if (n == 0): 
        return (sum1 == sum2) 
  
    # For every index i, we have two  
    # choices 
    # 1) We do not include arr[i] in first set 
    # 2) We include arr[i] in first set  
    # We return true if we can have 
    # sum equal in both sets  
    return isPossible(arr, n - 1, sum1 + arr[n - 1],  
                                sum2) or isPossible(arr, n - 1, sum1, sum2 + arr[n - 1]) 
  
# Returns true if arr can be partitioned  
# in two subsets of equal sum, otherwise  
# false 
def findPartion(arr, n): 
      
    # Calculate sum of the elements in array 
    sum1 = 0
    sum2 = 0
    for i in range(0, n):  
        sum1 = sum1 + arr[i] 
        sum2 = sum2 + arr[n-1-i]
    # If sum is odd, there cannot be two subsets  
    # with equal sum 
    if (sum1 % 2 != 0): 
        return False
  
    # Find if there is subset with  
    # sum equal to half of total sum 
    return isPossible(arr, n, 0, 0) 
  
# Driver code 
t=int(input())
while(t>0):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    n=len(arr)
    if (findPartion(arr, n)== True): 
        print(-1) 
    else:
        print(x)
    t=t-1