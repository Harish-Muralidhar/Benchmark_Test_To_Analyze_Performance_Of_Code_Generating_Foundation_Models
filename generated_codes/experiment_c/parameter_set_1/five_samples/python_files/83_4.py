'''

Explanation
The sample input corresponds to the example given in the problem
statement.


'''

def findSum(arr,n,P,K): 
  
    # Initialize curr_sum as value of first element 
    # and starting point as 0 
    curr_sum = arr[0] 
    start = 0
    i = 1
  
    # Add elements one by one to curr_sum and if the curr_sum exceeds K, 
    # then remove starting element 
    while i <= n: 
  
        # If curr_sum exceeds the K, then remove the starting elements
        while curr_sum >= K and start < i-1: 
            curr_sum = curr_sum - arr[start] 
            start += 1
          
        # If curr_sum becomes exactly K, then return curr_sum 
        if curr_sum >= K and start >= i-1: 
            return curr_sum%P 
              
        # Add this element to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
          
        # Increment count of elements 
        i += 1
    return -1

N,K,P=input().strip().split()
N,K,P=[int(N),int(K),int(P)]
arr=[]
for i in range(N):
    arr.append(int(input()))
print(findSum(arr,N,P,K))