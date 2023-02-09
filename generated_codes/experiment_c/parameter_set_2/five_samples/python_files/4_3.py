"""


"""

# Write your code here
import math

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(i,n):
            sum = 0
            prod = 1
            for k in range(i,j+1):
                sum += arr[k]
                prod *= arr[k]
            if sum == prod:
                count += 1
    print(count)