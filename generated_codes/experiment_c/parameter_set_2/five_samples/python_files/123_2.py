"""

Input:
2
4 9
4 4 2 6
4 2
4 4 2 6

Output:
1 4
0 0

Explanation:
Test case 1: The minimal possible absolute difference of 1 can be obtained by taking the pairs of a1 and a2, a1 and a4, a2 and a4, a3 and a4.
Test case 2: There are no pairs such that |ai + aj - K| is minimal possible.

"""

def find_min_diff(arr, k):
    arr.sort()
    i = 0
    j = len(arr) - 1
    min_diff = abs(arr[i] + arr[j] - k)
    count = 0
    while i < j:
        diff = abs(arr[i] + arr[j] - k)
        if diff < min_diff:
            min_diff = diff
            count = 1
        elif diff == min_diff:
            count += 1
        if arr[i] + arr[j] > k:
            j -= 1
        else:
            i += 1
    return min_diff, count


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = [int(i) for i in input().split()][0:2]
        arr = [int(i) for i in input().split()][0:n]
        min_diff, count = find_min_diff(arr, k)
        print(min_diff, count)