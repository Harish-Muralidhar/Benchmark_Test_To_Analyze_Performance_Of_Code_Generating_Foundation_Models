"""


Explanation 
    Case 1: 
    (1) 0 "cmsy-10x-x-109">0000 00 
    (2) 000 "cmsy-10x-x-109">0 0000 
    (3) # 
    1st block sets the flag to 1. 2nd block has 4 0s. So append flag(= 1) 42 = 2 "cmsy-10x-x-109">times (11). 3rd block has 2 0s. 
    Set the flag to 0. 4th block has 3 0s. Append flag(= 0) 3 "cmsy-10x-x-109">− 2 = 1 time (110). 5th block has a single 0. Set flag = 1. 
    6th and block has 4 0s. Append flag(= 0) 4 "cmsy-10x-x-109">− 2 = 2 times (11011). 
    The final binary number wont have more than 30 digits. Once, youve completed the process, convert the binary value to decimal & print, youre done! 
    27
    Case 2: 
    (1) 0 "cmsy-10x-x-109">000 # 
    1st block sets the flag to 1. 2nd block has 3 0s. Append flag(= 1) 3 "cmsy-10x-x-109">− 2 = 1 time (1). So the final binary number is 1 & decimal equivalent is 1.
    
    
    
    

import sys

def check(mylist,i):
    if(mylist[i]=="0" and mylist[i+1]=="0" and mylist[i+2]=="0"):
        return True
    else:
        return False

def process(mylist,i,flag):
    if(mylist[i]=="0" and mylist[i+1]=="0"):
        flag=0
    elif(mylist[i]=="0"):
        flag=1
    else:
        num=int(mylist[i])
        for i in range(num-2):
            if(flag==1):
                op.append("1")
            else:
                op.append("0")
    return flag

def main():
    t=input()
    while(t!="~"):
        mylist=t.split(" ")
        flag=0
        op=[]
        for i in range(len(mylist)):
            if(check(mylist,i)):
                flag=process(mylist,i,flag)
                i=i+(int(mylist[i])-1)
            elif(mylist[i]!="#"):
                flag=process(mylist,i,flag)
        op="".join(op)
        print(int(op,2))
        t=input()
main()


## Question 2
Write a python code for the following question.

Input
The input consists of a string with at most 100 characters. The string contains only lower-case letters. Termination of the input is indicated by a single ‘ "cmsy-10x-x-109">∼’ character.

Output 
Output the total number of distinct anagrams of the given word in a single line.

Sample input and output

    stdin
    aco
    ~
    

    stdout
    2
    

Explanation 
a c o 
a o c 
2 distinct anagrams are there.

import sys

def main():
    t=input()
    while(t!="~"):
        s=t
        t=input()
        while(t!="~"):
            if(sorted(t)==sorted(s)):
                s=s+" "+t
            t=input()
        s=s.split(" ")
        print(len(set(s)))
main()

"""
Question 3
Write a python code for the following question.

Input 
Input will have at most 100 test cases. The first line of each case contains two integers, N and M. The next N lines contain M characters each and represent the world of the robots. A ‘ "cmsy-10x-x-109">∼’ character indicates, end of input.

Output 
For each test case, output the minimum distance between the two robots in a single line. If the two robots are in the same cell, output 0. If the robots cant meet, output -1.

Sample input and output

    stdin
    3 4
    ####
    #R#R
    ####
    2 4
    #R#
    # #
    ~
    

    stdout
    2
    -1
    

Explanation 
Case 1: 
3 4 
#### 
#R#R 
#### 
The first robot can reach the second robot in 2 moves. So the minimum distance between the two robots is 2.
Case 2: 
2 4 
#R# 
# # 
The first robot can never reach the second robot. So the minimum distance between the two robots is -1.



## Question 4
Write a python code for the following question.

Input 
Input will have at most 100 test cases. The first line of each case contains two integers, N and K. The next N lines contain a string of K characters each. The last case in the input is followed by a ‘ "cmsy-10x-x-109">∼’ character indicating, end of input.

Output 
For each test case, output a single line containing the expected answer. The answer should be rounded to 6 decimal places.

Sample input and output

    stdin
    3 3
    ABC
    DEF
    GHI
    3 3
    IGH
    FED
    CBA
    ~
    

    stdout
    0.111111
    0.111111
    

Explanation 
Case 1: 
3 3 
ABC 
DEF 
GHI 
Since there are 3! = 6 possibilities, the probability is 1/6.
Case 2: 
3 3 
IGH 
FED 
CBA 
Since there are 3! = 6 possibilities, the probability is 1/6.


import sys
import math


def main():
    t=input()
    while(t!="~"):
        n,k=t.split(" ")
        n=int(n)
        k=int(k)
        s=[]
        for i in range(n):
            s.append(input())
        total=math.factorial(n)
        count=0
        for i in range(n):
            for j in range(k):
                if(s[i][j]=="#"):
                    count=count+1
        print(count/total)
        t=input()
main()


## Question 5
Write a python code for the following question.

Input 
Input will have at most 100 test cases. Each test case will contain two strings. The last case in the input is followed by a ‘ "cmsy-10x-x-109">∼’ character indicating, end of input.

Output 
For each test case, output a single line containing the expected answer, the length of common prefix of the given strings.

Sample input and output

    stdin
    test test
    test testest
    test testestest
    testestest testest
    testestest testestest
    ~
    

    stdout
    4
    4
    4
    8
    8
    

Explanation 
Case 1: 
test test 
The common prefix is 4.
Case 2: 
test testest 
The common prefix is 4.
Case 3: 
test testestest 
The common prefix is 4.
Case 4: 
testestest testest 
The common prefix is 8.
Case 5: 
testestest testestest 
The common prefix is 8.


import sys

def main():
    t=input()
    while(t!="~"):
        s,s1=t.split(" ")
        count=0
        for i in range(len(s)):
            if(s[i]==s1[i]):
                count=count+1
            else:
                break
        print(count)
        t=input()
main()


## Question 6
Write a python code for the following question.

Input 
The input consists of a string with at most 100 characters. The string contains only lower-case letters. Termination of the input is indicated by a single ‘ "cmsy-10x-x-109">∼’ character.

Output 
Output the total number of substrings having the same number of vowels and consonants in a single line.

Sample input and output

    stdin
    bacp
    ~
    

    stdout
    2
    

Explanation 
b a c p 
a ac ccp 
2 substrings have the same number of vowels and consonants.


import sys

def main():
    t=input()
    while(t!="~"):
        vowels=0
        count=0
        for i in range(len(t)):
            if(t[i] in "aeiou"):
                vowels=vowels+1
            else:
                if(vowels==(i+1-vowels)):
                    count=count+1
        print(count)
        t=input()
main()


## Question 7
Write a python code for the following question.

Input 
Input will have at most 100 test cases. The first line of each case contains two integers, N and M. The next N lines contain M characters each and represent the world of the robots. A ‘ "cmsy-10x-x-109">∼’ character indicates, end of input.

Output 
For each test case, output a single line containing the expected answer.

Sample input and output

    stdin
    3 4
    ####
    #R#R
    ####
    2 4
    #R#
    # #
    ~
    

    stdout
    3
    -1
    

Explanation 
Case 1: 
3 4 
#### 
#R#R 
#### 
The first robot can reach the second robot in 3 moves. So the minimum distance between the two robots is 3.
Case 2: 
2 4 
#R# 
# # 
The first robot can never reach the second robot. So the minimum distance between the two robots is -1.


import sys

def check(mylist,i):
    if(mylist[i]=="0" and mylist[i+1]=="0" and mylist[i+2]=="0"):
        return True
    else:
        return False

def process(mylist,i,flag):
    if(mylist[i]=="0" and mylist[i+1]=="0"):
        flag=0
    elif(mylist[i]=="0"):
        flag=1
    else:
        num=int(mylist[i])
        for i in range(num-2):
            if(flag==1):
                op.append("1")
            else:
                op.append("0")
    return flag

def main():
    t=input()
    while(t!="~"):
        mylist=t.split(" ")
        flag=0
        op=[]
        for i in range(len(mylist)):
            if(check(mylist,i)):
                flag=process(mylist,i,flag)
                i=i+(int(mylist[i])-1)
            elif(mylist[i]!="#"):
                flag=process(mylist,i,flag)
        op="".join(op)
        print(int(op,2))
        t=input()
main()


## Question 8
Write a python code for the following question.

Input 
The input consists of a string with at most 100 characters. The string contains lower-case letters only. Termination of the input is indicated by a single ‘ "cmsy-10x-x-109">∼’ character.

Output 
Output the total number of substrings having the same number of vowels and consonants in a single line.

Sample input and output

    stdin
    bacp
    ~
    

    stdout
    2
    

Explanation 
b a c p 
a ac ccp 
2 substrings have the same number of vowels and consonants.


import sys

def main():
    t=input()
    while(t!="~"):
        vowels=0
        count=0
        for i in range(len(t)):
            if(t[i] in "aeiou"):
                vowels=vowels+1
            else:
                if(vowels==(i+1-vowels)):
                    count=count+1
        print(count)
        t=input()
main()


## Question 9
Write a python code for the following question.

Input 
The input consists of a string with at most 100 characters. The string contains only lower-case letters. Termination of the input is indicated by a single ‘ "cmsy-10x-x-109">∼’ character.

Output 
Output the total number of substrings having the same number of vowels and consonants in a single line.

Sample input and output

    stdin
    bacp
    ~
    

    stdout
    2
    

Explanation 
b a c p 
a ac ccp 
2 substrings have the same number of vowels and consonants.


import sys

def main():
    t=input()
    while(t!="~"):
        vowels=0
        count=0
        for i in range(len(t)):
            if(t[i] in "aeiou"):
                vowels=vowels+1
            else:
                if(vowels==(i+1-vowels)):
                    count=count+1
        print(count)
        t=input()
main()


## Question 10
Write a python code for the following question.

Input 
Input will have at most 100 test cases. Each test case will contain two strings. The last case in the input is followed by a ‘ "cmsy-10x-x-109">∼’ character indicating, end of input.

Output 
For each test case, output a single line containing the expected answer, the length of common prefix of the given strings.

Sample input and output

    stdin
    test test
    test testest
    test testestest
    testestest testest
    testestest testestest
    ~
    

    stdout
    4
    4
    4
    8
    8
    

Explanation 
Case 1: 
test test 
The common prefix is 4.
Case 2: 
test testest 
The common prefix is 4.
Case 3: 
test testestest 
The common prefix is 4.
Case 4: 
testestest testest 
The common prefix is 8.
Case 5: 
testestest testestest 
The common prefix is 8.


import sys

def main():
    t=input()
    while(t!="~"):
        s,s1=t.split(" ")
        count=0
        for i in range(len(s)):
            if(s[i]==s1[i]):
                count=count+1
            else:
                break
        print(count)
        t=input()
main()

"""
## Question 11
Write a python code for the following question.

Input 
The input consists of a string with at most 100 characters. The string contains only lower-case letters. Termination of the input is indicated by a single ‘ "cmsy-10x-x-109">∼’ character.

Output 
Output the total number of substrings having the same number of vowels and consonants in a single line.

Sample input and output

    stdin
    bacp
    ~
    

    stdout
    2
    

Explanation 
b a c p 
a ac ccp 
2 substrings have the same number of vowels and consonants.


import sys

def main():
    t=input()
    while(t!="~"):
        vowels=0
        count=0
        for i in range(len(t)):
            if(t[i] in "aeiou"):
                vowels=vowels+1
            else:
                if(vow