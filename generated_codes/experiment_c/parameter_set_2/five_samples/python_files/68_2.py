'''


'''

# Write your code here

import sys

def subset(arr, n, sum): 
  
    if (sum == 0): 
        return 1
    if (n == 0 and sum != 0): 
        return 0
  
    if (arr[n - 1] > sum): 
        return subset(arr, n - 1, sum) 
  
    return subset(arr, n - 1, sum) + subset(arr, n - 1, sum - arr[n - 1]) 
  

def main():
    t = int(input())
    for i in range(t):
        n,q = map(int,input().split())
        arr = list(map(int,input().split()))
        for j in range(q):
            m = int(input())
            print(subset(arr,n,m))

main()