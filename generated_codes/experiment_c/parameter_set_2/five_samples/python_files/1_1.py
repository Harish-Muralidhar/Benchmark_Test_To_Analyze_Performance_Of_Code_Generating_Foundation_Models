"""

"""

def longest_alternating_subarray(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1,n):
        if arr[i]*arr[i-1]<0:
            dp[i] = dp[i-1]+1
    return dp

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(i) for i in input().split()][0:size]
        print(*longest_alternating_subarray(arr))