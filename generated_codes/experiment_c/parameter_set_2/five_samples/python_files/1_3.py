"""

"""

# Write your code here

def alternating_subarray(arr, n):
    res = [1] * n
    for i in range(1, n):
        if arr[i] * arr[i-1] < 0:
            res[i] = res[i-1] + 1
    return res

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*alternating_subarray(arr, n))