'''

Explanation:

The first number contains 4 occurences of the digit 4 (the first one from the left and three to the right of it).
The second number doesn't contain the digit.
The third number contains a single occurence of the digit 4.
The fourth number contains a single occurence of the digit 4 (the last one from the right).
The fifth number doesn't contain the digit 4.

'''

T = int(input())
for i in range(T):
    n = int(input())
    count = 0
    while n > 0:
        if n % 10 == 4:
            count += 1
        n = n // 10
    print(count)