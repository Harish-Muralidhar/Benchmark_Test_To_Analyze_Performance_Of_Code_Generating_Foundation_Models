"""

"""

# Write your code here
t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(2)
    else:
        print((n-1)*2 + n*(n-1))