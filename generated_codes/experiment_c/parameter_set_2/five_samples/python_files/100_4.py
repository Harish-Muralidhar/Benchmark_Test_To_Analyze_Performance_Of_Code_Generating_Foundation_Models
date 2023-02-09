"""


Solution:

"""

def subset_sum(arr, n, sum): 
    if (sum == 0): 
        return True
    if (n == 0 and sum != 0): 
        return False
    if (arr[n - 1] > sum): 
        return subset_sum(arr, n - 1, sum); 
    return subset_sum(arr, n - 1, sum) or subset_sum(arr, n - 1, sum - arr[n - 1]); 

def main():
    t=int(input())
    for i in range(t):
        n,m=map(int,input().split())
        arr=list(map(int,input().split()))
        if (subset_sum(arr, n, m) == True): 
            print("Yes") 
        else: 
            print("No") 
main()