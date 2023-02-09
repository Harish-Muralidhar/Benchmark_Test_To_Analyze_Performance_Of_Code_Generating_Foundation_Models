'''
'''
def reverse_integer(n):
    rev = 0
    while n != 0:
        r = n % 10
        rev = (rev * 10) + r
        n /= 10
    return rev

t = int(input())
for i in range(t):
    n = int(input())
    print(reverse_integer(n))