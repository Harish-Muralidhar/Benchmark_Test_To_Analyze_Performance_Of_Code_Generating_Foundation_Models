"""

Explanation
Example case 1. The sequence is already sorted, so the answer is YES.

Example case 2. The sequence is not sorted, so the answer is NO.

"""

# Write your code here

def almost_sorted(arr, n):
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            count += 1
    if count == 0 or count == 2:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(almost_sorted(arr, n))