"""
"""

#importing math module 
import math

#defining function for finding factorial of given number
def factorial_number(x):
    fact = math.factorial(x)
    return fact

#taking input number of test cases
T = int(input())
#declaring empty list
answer = []

#using while loop to take input data
while(T):
    #taking input number of elements in array
    N = int(input())
    #taking input array elements
    B = list(map(int,input().split()))
    #declaring empty list
    A = []
    #using for loop to take input data
    for i in range(N):
        #declaring value of a as 0
        a = 0
        #using for loop to take input data
        for j in range(i,N):
            #appending value a to list A
            A.append(a)
            #increasing value of a by one
            a = a + 1
    #initializing value of result as 1
    result = 1
    #using for loop to take input data
    for i in range(N):
        #calculating factorial of given number
        factorial_of_result = factorial_number(A[i])
        #calculating factorial of given number
        factorial_of_B = factorial_number(B[i])
        #calculating factorial of given number
        factorial_of_N = factorial_number(A[i]-B[i])
        #calculating factorial of given number
        final_result = factorial_of_result // (factorial_of_B * factorial_of_N)
        #multiplying result by final result
        result = result * final_result
        #taking modulo 1000000007 of result
        result = result % 1000000007
    #appending result to list answer
    answer.append(result)
    #decreasing value of T by one
    T = T - 1

#printing output as required
print(*answer)