'''


Sample Input 0

2
3
1 2 3
5
2 4 1 3 5
Sample Output 0

YES
NO


Explanation 0

Sample Case 1: The ordering is already sorted, therefore the answer is YES.

Sample Case 2: The ordering has two inversions, therefore the answer is NO.

'''

t = int(input())
for i in range(t):
    n = int(input())
    A = [int(i) for i in input().split(' ')]
    status = "YES"
    for i in range(n):
        if i == 0:
            if A[0] != A[1] and A[0] != A[1]-1:
                status = "NO"
        elif i > 0 and i < n-1:
            if A[i] != A[i+1] and A[i] != A[i+1]-1 and A[i] != A[i-1] and A[i] != A[i-1]+1:
                status = "NO"
        else:
            if A[-1] != A[-2] and A[-1] != A[-2]+1:
                status = "NO"
    print(status)