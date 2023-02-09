"""

=============================================================

My Answer:

import math
T = int(input())
for _ in range(T):
    A = int(input())
    B = math.sqrt(5*A**2 + 4)
    C = math.sqrt(5*A**2 - 4)
    if int(B)*int(B) == B**2 and int(C)*int(C) == C**2:
        print('YES')
    else:
        print('NO')
        
=============================================================

        OR

=============================================================

import math

def is_perfect_square(n):
    return n**0.5 == int(n**0.5)


def is_fibonacci(n):
    return is_perfect_square(5*n**2 + 4) or is_perfect_square(5*n**2 - 4)


T = int(input())
for _ in range(T):
    A = int(input())
    print("YES" if is_fibonacci(A) else "NO")
    
=============================================================
"""

# Answer 2:

"""

Write a python code for the following question.
Import the necessary libraries.
The Head Chef has been playing with Fibonacci numbers for long . He has learnt several tricks related to Fibonacci numbers . Now he wants to test his chefs in the skills . 
A fibonacci number is defined by the recurrence :
f(n) = f(n-1) + f(n-2) for n > 2 and f(1) = 0 and f(2) = 1 .  
Given a number  A   , determine if it is a fibonacci number.

Input

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The only line of each test case contains a single integer  A  denoting the number to be checked .


Output

For each test case, output a single line containing "YES" if the given number is a fibonacci number , otherwise output a single line containing "NO" . 


Constraints

1 ≤ T ≤ 1000
1 ≤ number of digits in A  ≤ 1000
  The sum of number of digits in A in all test cases   <= 10000.  


Example
Input:
3
3
4
5

Output:
YES
NO
YES

Explanation
Example case 1. The first few fibonacci numbers are 0 , 1 , 1 , 2 , 3 ,5 , 8 , 13 and so on and the series is increasing . Only 3 and 5 appear in this series while 4 does not appear in the series . 

=============================================================

My Answer:

T = int(input())
for _ in range(T):
    A = int(input())
    if A in [0, 1]:
        print('YES')
    elif A == 2:
        print('NO')
    else:
        fib = [0, 1]
        for i in range(2, A):
            fib.append(fib[i-1] + fib[i-2])
        if A in fib:
            print('YES')
        else:
            print('NO')
            
=============================================================
"""

# Answer 3:

"""

Write a python code for the following question.
Import the necessary libraries.
The Head Chef has been playing with Fibonacci numbers for long . He has learnt several tricks related to Fibonacci numbers . Now he wants to test his chefs in the skills . 
A fibonacci number is defined by the recurrence :
f(n) = f(n-1) + f(n-2) for n > 2 and f(1) = 0 and f(2) = 1 .  
Given a number  A   , determine if it is a fibonacci number.

Input

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The only line of each test case contains a single integer  A  denoting the number to be checked .


Output

For each test case, output a single line containing "YES" if the given number is a fibonacci number , otherwise output a single line containing "NO" . 


Constraints

1 ≤ T ≤ 1000
1 ≤ number of digits in A  ≤ 1000
  The sum of number of digits in A in all test cases   <= 10000.  


Example
Input:
3
3
4
5

Output:
YES
NO
YES

Explanation
Example case 1. The first few fibonacci numbers are 0 , 1 , 1 , 2 , 3 ,5 , 8 , 13 and so on and the series is increasing . Only 3 and 5 appear in this series while 4 does not appear in the series . 

=============================================================

My Answer:

T = int(input())
for _ in range(T):
    A = int(input())
    fib = [0, 1]
    for i in range(2, A):
        fib.append(fib[i-1] + fib[i-2])
    if A in fib:
        print('YES')
    else:
        print('NO')
        
=============================================================
"""