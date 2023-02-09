'''

Explanation

Example case 1. The sequence is already sorted, so the answer is YES.

Example case 2. The distance between the current position of any value and its correct position is at most 1.

Example case 3. The distance between the current position of a[3] and its correct position is 2.

Example case 4. The distance between the current position of a[4] and its correct position is 3.

Example case 5. The distance between the current position of a[5] and its correct position is 4.

Hence, the answer is NO.

'''

#code

def almost_sorted(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            count += 1
            if count > 2:
                return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if almost_sorted(arr):
        print('YES')
    else:
        print('NO')