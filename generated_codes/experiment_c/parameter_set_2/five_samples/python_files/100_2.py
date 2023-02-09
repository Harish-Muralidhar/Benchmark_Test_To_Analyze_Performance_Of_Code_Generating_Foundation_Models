"""


"""

# Write your code here

def find_subset(arr, n, sum): 
    if (sum == 0): 
        return True
    if (n == 0 and sum != 0): 
        return False
    if (arr[n-1] > sum): 
        return find_subset(arr, n-1, sum) 
    return find_subset(arr, n-1, sum) or find_subset(arr, n-1, sum-arr[n-1]) 

def main():
    t = int(input())
    while t > 0:
        n,m = map(int, input().split())
        arr = list(map(int, input().split()))
        if find_subset(arr, n, m):
            print("Yes")
        else:
            print("No")
        t -= 1

if __name__ == "__main__":
    main()