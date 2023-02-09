'''

Explanation

Testcase 1: Sum of each of the digits of the number 12345 is 1+2+3+4+5 = 15
'''
n=int(input())
sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=n/10
print(int(sum))