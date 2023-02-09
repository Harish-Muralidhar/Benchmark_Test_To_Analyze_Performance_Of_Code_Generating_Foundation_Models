"""

Explanation
Example case 1. The sequence is already sorted, so the answer is YES.

Example case 2. The sequence is not sorted in an increasing order, so the answer is NO.
"""

# Program Code:

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    flag = 0
    for i in range(n):
        if(abs(arr[i]-i-1)>1):
            flag += 1
    if(flag == 0):
        print("YES")
    else:
        print("NO")