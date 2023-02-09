"""

"""

# Write your code here
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    for j in range(n):
        if a[j] >= b[j]:
            count += 1
    print(count)