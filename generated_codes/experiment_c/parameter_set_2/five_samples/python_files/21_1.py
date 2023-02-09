'''

Explanation

In the first test case, 1 divided by 2 has a remainder of 1.
In the second test case, remainder is 100 when 10 is divided by 200.
In the third test case, remainder is 10 when 10 is divided by 40.

'''

#code

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    print(a%b)