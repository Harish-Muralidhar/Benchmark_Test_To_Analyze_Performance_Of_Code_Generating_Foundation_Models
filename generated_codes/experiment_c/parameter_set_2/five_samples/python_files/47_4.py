'''

Explanation
The list contains 5 integers. For the first number, 4 occurs four times in the decimal representation of 447474 (the digits 7 and 4 appear twice, but we don't count them twice). For the second number, there are no occurences of 4. For the third number, 4 occurs once in the decimal representation of 6664. For the fourth number, 4 occurs once in the decimal representation of 40. For the fifth number, there are no occurences of 4.

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
The list contains 5 integers. For the first number, 4 occurs four times in the decimal representation of 447474 (the digits 7 and 4 appear twice, but we don't count them twice). For the second number, there are no occurences of 4. For the third number, 4 occurs once in the decimal representation of 6664. For the fourth number, 4 occurs once in the decimal representation of 40. For the fifth number, there are no occurences of 4.

'''

# Write your code here

def count_four(n):
    count = 0
    while n > 0:
        if n % 10 == 4:
            count += 1
        n = n // 10
    return count

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_four(n))