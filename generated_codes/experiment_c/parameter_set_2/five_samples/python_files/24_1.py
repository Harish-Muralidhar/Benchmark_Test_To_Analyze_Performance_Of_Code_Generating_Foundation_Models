'''

'''

#Solution

def sumOfDigits(n):
    sum = 0
    while(n > 0):
        sum = sum + n % 10
        n = n // 10
    print(sum)

t = int(input())
for i in range(t):
    n = int(input())
    sumOfDigits(n)