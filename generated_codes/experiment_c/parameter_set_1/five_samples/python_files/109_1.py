"""

import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

for t in range(int(raw_input())):
    N = int(raw_input())
    k = int(math.ceil(math.sqrt(N)))
    for i in range(k, N):
        for j in range(i, N):
            if is_prime(i) and is_prime(j) and i+2*j == N:
                print "YES"
                break
    else:
        print "NO"
"""

"""
Theory of Everything

The goal of this problem is to print the formula for the "Theory of Everything"

Input
Input contains a single integer N.

Output
Output a single line containing the formula for the "Theory of Everything", with no spaces. Each element of the formula is separated by a '+' sign.

Constraints
1 ≤ N ≤ 20

Example
Input:
3

Output:
1/1+1/2+1/3

Input:
20

Output:
1/1+1/2+1/3+1/4+1/5+1/6+1/7+1/8+1/9+1/10+1/11+1/12+1/13+1/14+1/15+1/16+1/17+1/18+1/19+1/20

n=int(raw_input())
for i in range(1,n+1):
    print "1/%d+"%i,
"""

"""
Write a python code for the following question.
Vineet has recently started giving online tests. The online test consists of N questions and Vineet has to answer all the questions.

After submitting the answer for a question, Vineet is given only two options

Accept: Accept the answer given by him.
Reject: Reject the answer given by him and choose to skip the question. By skipping the question, Vineet is not allowed to attempt the question again and will receive a score of 0 for the question.
The score for a question is the number of points Vineet receives for answering the question correctly. Vineet's final score for the test is the sum of all the scores for the questions he has attempted. Vineet's score is the total score of all the questions he has attempted, divided by the total number of questions he has attempted.

Vineet wants to maximize his score. Help Vineet to determine the maximum score he can receive.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains an integer N denoting the number of questions in the online test. The second line contains N space separated integers denoting the score of the questions.

Output

For each test case, output a single line containing the maximum score Vineet can receive. The answer will be considered correct if it has an absolute error less than 10-6.

Constraints

1 ≤ T ≤ 10
1 ≤ N ≤ 10^5
1 ≤ Score of each question ≤ 10^5


Example
Input:
2
3
1 2 3
3
1 4 7

Output:
1.6666666666666667
2.5

Explanation

For the first test case, Vineet may attempt all three questions. His score will be (1+2+3)/3 = 2.

For the second test case, Vineet's best option is to attempt the first 2 questions. His score will be (1+4)/2 = 2.5.

import math

for _ in range(int(raw_input())):
    n = int(raw_input())
    score = map(int, raw_input().split())
    score.sort()
    score = score[::-1]
    if score[0] < score[1]:
        print round(float(sum(score[0:2]))/2, 6)
    else:
        print round(float(sum(score[0:3]))/3, 6)
"""

"""
Chef and his Location

Chef has a long string S of lowercase English letters. He needs to find the location of the lexicographically smallest non-empty substring of S that contains all the vowels ('a', 'e', 'i', 'o', 'u', in this order).

The location of a substring is the 1-based index of its first character. For example, the locations of the substrings "c" and "bc" in the string "abc" are 1 and 2, respectively.

Chef does not need to find the lengths of the substrings. He only needs their locations.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a single string S with length N.

Output
For each test case, print a single line containing one integer ― the location of the lexicographically smallest non-empty substring of S that contains all the vowels ('a', 'e', 'i', 'o', 'u', in this order).

Constraints
1 ≤ T ≤ 10
1 ≤ N ≤ 105
Subtasks
Subtask #1 (10 points): it is guaranteed that the location of a substring is between 1 and n
Subtask #2 (90 points): original constraints

Example
Input:
1
16
chefandhislocation

Output:
2

Explanation
Example case 1: The lexicographically smallest non-empty substring of S="chefandhislocation" that contains all the vowels is "andhis". Its location is 2.

for _ in range(int(raw_input())):
    n = int(raw_input())
    S = raw_input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(n):
        if S[i] in vowel:
            index = vowel.index(S[i])
            for j in range(i+1, n):
                if S[j] in vowel:
                    if vowel.index(S[j]) == index+1:
                        index += 1
            if index == 4:
                print i+1
                break
"""

"""
import math

for _ in range(int(raw_input())):
    n = int(raw_input())
    S = raw_input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(n):
        if S[i] in vowel:
            index = vowel.index(S[i])
            for j in range(i+1, n):
                if S[j] in vowel:
                    if vowel.index(S[j]) == index+1:
                        index += 1
            if index == 4:
                print i+1
                break
"""

"""
import math

for _ in range(int(raw_input())):
    n = int(raw_input())
    S = raw_input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(n):
        if S[i] in vowel:
            index = vowel.index(S[i])
            for j in range(i+1, n):
                if S[j] in vowel:
                    if vowel.index(S[j]) == index+1:
                        index += 1
            if index == 4:
                print i+1
                break
"""


"""
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b / gcd(a, b)

for _ in range(int(raw_input())):
    n = int(raw_input())
    S = map(int, raw_input().split())
    lcm = 1
    for i in range(n):
        lcm = lcm(lcm, S[i])
    print lcm
"""

"""
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b / gcd(a, b)

for _ in range(int(raw_input())):
    n = int(raw_input())
    S = map(int, raw_input().split())
    lcm = 1
    for i in range(n):
        lcm = lcm(lcm, S[i])
    print lcm
"""

"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

def lcm(a, b):
    return a * b / gcd(a, b)

for _ in range(int(raw_input())):
    n = int(raw_input())
    S = map(int, raw_input().split())
    lcm = 1
    for i in range(n):
        lcm = lcm(lcm, S[i])
    print lcm
"""

"""
Chef and Factorization

Chef is a teacher at a reputed school. He is known for being a strict teacher. He asks his students to solve all the problems given in the problem set, without fail. There are N students in his class. He gives each student the same problem set.

There are M problems in the problem set. The problem set consists of M questions, given in the form of an array A1, A2, ..., AM. Each of the M questions is a number. The problems are arranged in a row, in the order they appear in the problem set.

An array B1, B2, ..., BM is defined as a non-empty contiguous sub-array of A1, A2, ..., AM, if there are integers P and Q such that B1 = AP, B2 = AP+1, ..., BM = AP+M-1.

Chef gives marks to his students based on their performance in the test. For a student, the number of marks given by Chef is equal to the number of non-empty contiguous sub-arrays of A1, A2, ..., AM, such that for each B1, B2, ..., BM, the condition gcd(B1, B2, ..., BM) = 1 is satisfied.

Chef is curious to know the maximum marks he can give to a student. Please help him in finding the answer.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M.
The second line contains M space-separated integers A1, A2, ..., AM.

Output
For each test case, print a single line containing one integer ― the maximum marks Chef can give to a student.

Constraints
1 ≤ T ≤ 5
1 ≤ N ≤ 200
1 ≤ M ≤ 200
1 ≤ Ai ≤ 106 for each valid i

Subtasks
Subtask #1 (20 points):

1 ≤ T ≤ 2
1 ≤ N, M ≤ 2
1 ≤ Ai ≤ 10 for each valid i
Subtask #2 (80 points): original constraints

Example Input
3
2 4
1 2 3 4
1 4
2 3 4 5
2 4
1 3 7 5

Example Output
10
4
12

Explanation
Example case 1:

All the non-empty contiguous sub-arrays of the array [1, 2, 3, 4] are listed below, along with their gcd's.

[1] : gcd is 1.
[2] : gcd is 2.
[3] : gcd is 3.
[4] : gcd is 4.
[1, 2] : gcd is 1.
[2, 3] : gcd is 1.
[3, 4] : gcd is 1.
[1, 2, 3] : gcd is 1.
[2, 3, 4] : gcd is 1.
[1, 2, 3, 4] : gcd is 1.

Since all the gcd's are equal to 1, Chef will give 10 marks to his students.

T = int(raw_input())

for _ in range(T):
    N, M = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = [[] for i in range(M+1)]
    B[0] = [1]
    for i in range(1, M+1):
        for j in range(i):
            if gcd(A[j], A[i-1]) == 1:
                B[i].append(B[j][-1]+1)

    print max(B[M])
"""

"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

T = int(raw_input())

for _ in range(T):
    N, M = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = [[] for i in range(M+1)]
    B[0] = [1]
    for i in range(1, M+1):
        for j in range(i):
            if gcd(A[j], A[i-1]) == 1:
                B[i].append(B[j][-1]+1)

    print max(B[M])
"""

"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

T = int(raw_input())

for _ in range(T):
    N, M = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = [[] for i in range(M+1)]
    B[0] = [1]
    for i in range(1, M+1):
        for j in range(i):
            if gcd(A[j], A[i-1]) == 1:
                B[i].append(B[j][-1]+1)

    print max(B[M])
"""

"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

T = int(raw_input())

for _ in range(T):
    N, M = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = [[] for i in range(M+1)]
    B[0] = [1]
    for i in range(1, M+1):
        for j in range(i):
            if gcd(A[j], A[i-1]) == 1:
                B[i].append(B[j][-1]+1)

    print max(B[M])
"""

"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

T = int(raw_input())

for _ in range(T):
    N, M = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = [[] for i in range(M+1)]
    B[0] = [1]
    for i in range(1, M+1):
        for j in range(i):
            if gcd(A[j], A[i-1]) == 1:
                B[i].append(B[j][-1]+1)

    print max(B[M])
"""

"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b:
        a