'''

Explanation

The first number contains 4 occurences of 4, the second number has 0 occurences, and so on.

'''

# Write your code here

def count_4(n):
    count = 0
    while n > 0:
        if n % 10 == 4:
            count += 1
        n = n // 10
    return count

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(count_4(num))