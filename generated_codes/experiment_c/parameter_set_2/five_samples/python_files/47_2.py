'''

Explanation
The list contains 5 integers. For the first number, 4 occurs four times in its decimal representation, the second number contains no occurences of the digit 4, and so on.

Sample Input
5
447474
228
6664
40
81

Sample Output
4
0
1
1
0

Explanation
The list contains 5 integers. For the first number, 4 occurs four times in its decimal representation, the second number contains no occurences of the digit 4, and so on.

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