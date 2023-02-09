"""

Input:
2
4 9
4 4 2 6
3 7
1 2 3

Output:
1 4
0 1

Explanation:
Test case 1.
The minimal possible absolute difference of 1 can be obtained by taking the pairs of a1 and a2, a1 and a4, a2 and a4, a3 and a4.
Test case 2.
The minimal possible absolute difference of 0 can be obtained by taking the pair of a1 and a3.

"""

# Write your code here
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    min_diff = float('inf')
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(arr[i]+arr[j]-k) < min_diff:
                min_diff = abs(arr[i]+arr[j]-k)
                count = 1
            elif abs(arr[i]+arr[j]-k) == min_diff:
                count += 1
    print(min_diff,count)