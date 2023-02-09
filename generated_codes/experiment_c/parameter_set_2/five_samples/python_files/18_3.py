"""

"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def trailing_zeros(n):
    count = 0
    while n > 0:
        n = n//5
        count += n
    return count

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num = int(input())
        print(trailing_zeros(num))