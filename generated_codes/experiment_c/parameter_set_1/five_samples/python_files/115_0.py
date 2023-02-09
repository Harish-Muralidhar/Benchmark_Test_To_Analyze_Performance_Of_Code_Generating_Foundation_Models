"""

Solution

Test Case 1

2
10 12

Total operations performed:

( 12 - 10 ) => 2
( 10 - 2 ) => 8
( 8 - 2 ) => 6
( 6 - 2 ) => 4
( 4 - 2 ) => 2

Terminal value: 2

Test Case 2

2
5 9

Total operations performed:

( 9 - 5 ) => 4
( 5 - 4 ) => 1
( 4 - 1 ) => 3
( 3 - 1 ) => 2
( 2 - 1 ) => 1

Terminal value: 1

Test Case 3

3
6 10 15

Total operations performed:

( 15 - 6 ) => 9
( 10 - 6 ) => 4
( 9 - 6 ) => 3
( 9 - 3 ) => 6
( 6 - 4 ) => 2
( 6 - 2 ) => 4
( 4 - 2 ) => 2
( 4 - 2 ) => 2
( 2 - 2 ) => 0
( 2 - 2 ) => 0
( 2 - 1 ) => 1
( 1 - 1 ) => 0

Terminal value: 1

Algorithm

We can observe that the number of operations performed is independent of the manner in which the game is played.

The number of operations performed is equal to the number of times the largest number changes.

For example, in the first test case, the largest number changes 5 times. In the second test case, the largest number changes 5 times. In the third test case, the largest number changes 10 times.

The total number of operations performed is equal to the number of times the largest number changes.

The value of the largest number is reduced by one every time it changes. The value of the largest number after the kth operation is equal to the value of the largest number before the kth operation minus k.

To find the number of times the largest number changes, we need to find the number of integers that are greater than or equal to (largest_number - operations_performed).

If we subtract the largest number from each integer in the sequence, the number of integers greater than or equal to largest_number - operations_performed will be equal to the number of integers greater than or equal to 0.

For example, in the third test case, the largest number changes 10 times. The largest number after the 10th operation is equal to 6 - 10 = -4.

The number of integers greater than or equal to -4 is equal to the number of integers greater than or equal to 0.

It is easy to find the number of integers greater than or equal to 0. Subtracting the largest number from each integer in the sequence will not change the ordering of the integers.

Find the largest number in the sequence. Subtract this number from each integer in the sequence. Count the number of integers greater than or equal to 0. Add 1 to this count.

The sequence of numbers after the game terminates will be equal to the number obtained in the previous step repeated enough times so that all the numbers are equal.
"""

def operations(a):
    a_max = max(a)
    a_len = len(a)
    return a_len - len(list(filter(lambda x: x >= a_max - a_len + 1, a)))

def terminal_value(a):
    return operations(a) + 1

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(terminal_value(a))