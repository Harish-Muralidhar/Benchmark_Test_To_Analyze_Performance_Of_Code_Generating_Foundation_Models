'''

'''

# Write your code here

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for i in range(t):
    n = int(input())
    print(factorial(n))