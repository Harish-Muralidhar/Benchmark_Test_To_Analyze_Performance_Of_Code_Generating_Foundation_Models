'''


# Write your code here

import math
t = int(input())
for i in range(t):
    n = int(input())
    fac = math.factorial(n)
    print(fac)'''

'''

# Write your code here

import math
t = int(input())
for i in range(t):
    n = int(input())
    fac = math.factorial(n)
    print(fac)'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

Input Format:

A single line of input containing the full name, S.

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalised. Example 12abc when capitalised remains 12abc.

Output Format:

Print the capitalized string, S.

Sample Input

chris alan

Sample Output

Chris Alan
'''

'''
def solve(s):
    t = s.split(" ")
    for i in range(len(t)):
        if t[i]:
            t[i] = t[i].capitalize()
    print(" ".join(t))

s = input()
result = solve(s)
'''

'''

Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 


The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__

Subject 1   |  89    90    78    93    80

Subject 2   |  90    91    85    88    86

Subject 3   |  91    92    83    89    90.5

Average        90    91    82    90    85.5

Input Format:

The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject.

Constraints

0 < N <= 100
0 < X <= 100

Output Format:

Print the averages of all students on separate lines.

The averages must be correct up to 1 decimal place.

Sample Input

5 3

89 90 78 93 80

90 91 85 88 86

91 92 83 89 90.5

Sample Output

90.0

91.0

82.0

90.0

85.5
'''

'''
n, x = map(int, input().split())
sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) )

for i in zip(*sheet):
    print( sum(i)/len(i) )
'''

'''

Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 


You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format:

A single line containing the string S and integer value k separated by a space.

Constraints

0 < k <= len(S)

The string contains only UPPERCASE characters.

Output Format:

Print the different combinations of string S on separate lines.

Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''

'''
from itertools import combinations

s,k = input().split()

for i in range(1, int(k)+1):
    for j in combinations(sorted(s),i):
        print("".join(j))

'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Consider that vowels in the alphabet are a, e, i, o, u and y.

Function score_words takes a list of lowercase words as an argument and returns a score as follows:
The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1. The score for the whole list of words is the sum of scores of all words in the list.
Debug the given function score_words such that it returns a correct score.

Your function will be tested on several cases by the locked template code.

Input Format:

The input is read by the provided locked code template. In the first line, there is a single integer n denoting the number of words. In the second line, there are n space-separated lowercase words.

Constraints

2 ≤ n ≤ 20
Each word has at most 20 letters and all letters are English lowercase letters

Output Format:

The output is produced by the provided and locked code template. It calls function score_words with the list of words read from the input as the argument and prints the returned score to the output.

Sample Input 0

2
hacker book

Sample Output 0

4

Explanation 0

The two words are "hacker" and "book". Given that vowels in the alphabet are a, e, i, o and u, "hacker" contains an even number of vowels, namely three, so the score for this word is 2. "book" also contains three vowels, so the score for this word is also 2. The sum of scores for the two words is 2 + 2 = 4.

Sample Input 1

2
programming is awesome

Sample Output 1

4

Explanation 1

"programming" contains 3 vowels and hence gets a score of 2. "is" also has a score of 2. The sum is 4.

Sample Input 2

3
a bb c

Sample Output 2

2

Explanation 2

Only the first word has an even number of vowels, so this is the only word that gets a score of 2. The sum is 2.

'''
'''def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1
    return score


n = int(input())
words = input().split()
print(score_words(words))'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3

Sample Output 0

Weird

Sample Input 1

24

Sample Output 1

Not Weird
'''
'''
N = int(input())
if N%2 != 0:
    print("Weird")
elif N in range(2,6):
    print("Not Weird")
elif N in range(6,21):
    print("Weird")
elif N > 20:
    print("Not Weird")
'''

'''

Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

You are given a class Solution and its main method in the editor. Your task is to create a class Prime. The class Prime should contain a single method checkPrime.

The locked code in the editor will call the checkPrime method with one or more integer arguments. You should write the checkPrime method in such a way that the code prints only the prime numbers.

Please read the code given in the editor carefully. Also please do not use method overloading!

Note: You may get a compile time error in this problem due to the statement below:

  BufferedReader br=new BufferedReader(new InputStreamReader(in));
This was added intentionally, and you have to figure out a way to get rid of the error.

Input Format:

There are only five lines of input, each containing one integer.

Output Format:

There will be only four lines of output. Each line contains only prime numbers depending upon the parameters passed to checkPrime in the main method of the class Solution. In case there is no prime number, then a blank line should be printed.

Sample Input

2
1
3
4
5

Sample Output

2 
2 
2 3 
2 3 5 

Explanation

In the first two cases, the prime numbers are only 2. In the third case, the prime numbers are 2 and 3. In the fourth case, the prime numbers are 2,3, and 5.
'''
'''
def check_prime(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False

T=int(input())
for i in range(T):
    number = int(input())
    if check_prime(number):
        print(number)
'''
'''

Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 


A Python function, isSubsetSum (int set[], int n, int sum), that returns true if there is a subset of set[] with sum equal to given sum.

Input:

The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'N' denoting the size of the array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array. The third line contains an integer 'sum' denoting the sum of the two numbers.

Output:

Print "1" if there is a subset of set[] with sum equal to given sum, else print "0" (without quotes).

Constraints:

1 <= T <= 100
1 <= N <= 100
1 <= set[i] <= 200

Example:

Input:

2
6
2 3 5 6 8 10
10
5
1 2 3 4 5
10

Output:

1
1

Explanation:
Testcase1: There is a subset (2, 3, 5) with sum 10.
Testcase2: There is a subset (4, 5) with sum 9.
'''
'''
def isSubsetSum(set,n,sum):
    subset =([[False for i in range(sum+1)] for i in range(n+1)])

    for i in range(n+1):
        subset[i][0] = True

    for i in range(1,sum+1):
        subset[0][i] = False

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>=set[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i-1][j-set[i-1]])

    return subset[n][sum]

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sum = int(input())
    if(isSubsetSum(arr,n,sum) == True):
        print("1")
    else:
        print("0")'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Input Format:

First line contains T, the number of testcases. This is followed by T lines each containing an integer N.

Constraints

1 <= T <= 100
1 <= N <= 10000
Output Format:

Print the answer for each testcase in a new line.

Sample Input 0

2
12
13

Sample Output 0

3
2

Explanation 0

12 can be represented as 4+4+4. 13 can be represented as 4+9

'''
'''
import sys
import math

def numSquares(n):
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    a = 0
    while a*a <= n:
        b = int(math.sqrt(n - a*a))
        if a*a + b*b == n:
            return (not not a) + (not not b)
        a += 1
    return 3

t = int(input())
for i in range(t):
    n = int(input())
    print(numSquares(n))
'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format:

The first and only line contains the integer, .

Constraints:

Output Format:

Print  lines, one corresponding to each .

Sample Input 0

5

Sample Output 0

0
1
4
9
16

'''
'''
n = int(input())
for i in range(n):
    print(i*i)
'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format:

The first line contains a string consisting of space separated words.

Output Format:

Print the formatted string as explained above.

Sample Input 0

this is a string

Sample Output 0

this-is-a-string

'''
'''
def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
'''

'''
Write a python code for the following question.
Import the necessary libraries.

A tutorial for this problem is now available on our blog. Click here to read it. 

You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:

Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
'''
'''
def palindrome(string):
    for i in range(len(string)):
        if(string[i] != string[-i-1]):
            return False
    return True

def get_minimum_characters(string):
    if palindrome(string):
        return 0
    else:
        return 1

string = input()
print(get_minimum_characters(string))
'''

'''
Write a python