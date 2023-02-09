"""

"""

def alternating_subarray(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        if (arr[i] < 0 and arr[i-1] > 0) or (arr[i] > 0 and arr[i-1] < 0):
            dp[i] = dp[i-1] + 1
    return dp

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*alternating_subarray(arr))