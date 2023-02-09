"""

Explanation

Test Case 1
First Digit = 1
Last Digit = 4
Sum = First Digit + Last Digit = 1 + 4 = 5

Test Case 2
First Digit = 1
Last Digit = 4
Sum = First Digit + Last Digit = 1 + 4 = 5

Test Case 3
First Digit = 2
Last Digit = 3
Sum = First Digit + Last Digit = 2 + 3 = 5

"""

#code
t = int(input())
for i in range(t):
    n = input()
    print(int(n[0])+int(n[-1]))