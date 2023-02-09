'''
'''

#Solution

#for i in range(int(input())):
#    print(sum([int(a) for a in str(input())]))

#Problem Set II:
'''
Problem Statement
Write a python program to solve the following problem statement.

Consider the following series:

1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, …

This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order. 
Write a program to find the Nth term in this series.

Input Format
The first line contains an integer T, the number of test cases.
The next T lines contains an integer N.

Output Format
Print exactly one line per test case. The Nth term in the series.

Constraints
1 <= T <= 50
1 <= N <= 100

Example
Input:
3
7
10
15

Output:
13
29
47
'''

#Solution

#from math import sqrt

#def isprime(number):
#    for i in range(2, int(sqrt(number))+1):
#        if number % i == 0:
#            return False
#    return True

#def fibonacci(limit):
#    a = 1
#    b = 2
#    while a < limit:
#        yield a
#        c = a + b
#        a = b
#        b = c

#def nthterm(number):
#    if number % 2 == 0:
#        count = 1
#        for i in range(3, number+1):
#            if isprime(i):
#                count += 1
#            if count == number // 2:
#                yield i
#    else:
#        count = 1
#        for i in fibonacci(number):
#            if count == number // 2 + 1:
#                yield i
#            count += 1

#t = int(input())
#for i in range(t):
#    n = int(input())
#    print(list(nthterm(n))[0])
    
    
#Problem Set III:
'''
Problem Statement
Write a program to solve the following problem statement.

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints:
The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

#Solution

#n = int(input())
#l = []
#for _ in range(n):
#    s = input().split()
#    cmd = s[0]
#    args = s[1:]
#    if cmd !="print":
#        cmd += "("+ ",".join(args) +")"
#        eval("l."+cmd)
#    else:
#        print(l)


#Problem Set IV:
'''
Problem Statement
Write a python program to solve the following problem statement.

You are given an integer N. You have to find whether N is a perfect square or not.

Input Format
The first line contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be checked.

Output Format
For each test case, print "YES" if N is a perfect Square else print "NO".

Constraints
1 <= T <= 10^4
1 <= N <= 10^9

Sample Input

3
3
5
7

Sample Output

NO
YES
NO
'''

#Solution

#import math
#t = int(input())
#for i in range(t):
#    n = int(input())
#    s = math.sqrt(n)
#    if s-int(s)==0:
#        print("YES")
#    else:
#        print("NO")

#Problem Set V:
'''
Problem Statement
Write a python program to solve the following problem statement.

Given an integer N, find and return the count of minimum numbers, sum of whose squares is equal to N.

Output Format
Return the count of minimum numbers, sum of whose squares is equal to N.

Constraints
1 <= N <= 100000

Sample Input

11

Sample Output

3

'''

#Solution

#import math
#n = int(input())
#c=0
#for i in range(1,int(math.sqrt(n))+1):
#    if n%i==0:
#        c+=1
#if math.sqrt(n)-int(math.sqrt(n))==0:
#    print(2*c-1)
#else:
#    print(2*c)

#Problem Set VI:
'''
Problem Statement
Write a python program to solve the following problem statement.

Given a list A of N integers. The task is to eliminate the minimum number of elements such that in the resulting list the sum of any two adjacent values is even.

Numbers = [1, 3, 5, 4, 2] Output = [1, 3, 5] Total elements removed 2 Elements to be removed [4,2]

Input Format
First line contains integer N, denoting number of elements in list A.
Second line contains N integers, denoting the elements of list A.

Output Format
Print the minimum number of elements that need to be deleted to make the sum of any two adjacent values even.

Constraints
2 <= N <= 100
1 <= A[i] <= 106

Sample Input

6
1 3 5 4 2 2

Sample Output

2
'''

#Solution

#n = int(input())
#l = list(map(int, input().split()))
#c=0
#for i in range(len(l)):
#    if l[i]%2==0:
#        l[i]=0
#    else:
#        c+=1
#if c%2==0:
#    print(0)
#else:
#    print(1)

#Problem Set VII:
'''
Problem Statement
Write a python program to solve the following problem statement.

Given a number N followed by N numbers. Find the difference between the maximum and minimum of the numbers.

Input Format
The first line contains N, where N is the number of numbers.
The next line contains N integers.

Output Format
Print the difference between the maximum and minimum of the N numbers.

Constraints
1 <= N <= 100

Sample Input

3
3 4 1

Sample Output

3
'''

#Solution

#n = int(input())
#l = list(map(int, input().split()))
#print(max(l)-min(l))

#Problem Set VIII:
'''
Problem Statement
Write a python program to solve the following problem statement.

Given a number N followed by N numbers. Find the difference between the sum of the even numbers and the odd numbers.

Input Format
The first line contains N, where N is the number of numbers.
The next line contains N integers.

Output Format
Print the difference between the sum of the even numbers and the odd numbers.

Constraints
1 <= N <= 100

Sample Input

3
3 4 1

Sample Output

-2
'''

#Solution

#n = int(input())
#l = list(map(int, input().split()))
#even=0
#odd=0
#for i in range(n):
#    if l[i]%2==0:
#        even+=l[i]
#    else:
#        odd+=l[i]
#print(even-odd)