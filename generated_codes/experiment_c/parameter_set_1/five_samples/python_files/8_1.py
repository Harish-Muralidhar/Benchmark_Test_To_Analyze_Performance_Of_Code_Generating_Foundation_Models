
The solution is provided in the following code:
<code>import sys

n=int(input())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    if a&lt;b:
        print('&lt;')
    elif a&gt;b:
        print('&gt;')
    elif a==b:
        print('=')
</code>
But this solution is giving the correct answer for all the test cases but the output is not accepted by the online judge.
I am using python 3.6
Please help me out.
Thanks in advance.


A:

you need <code>'&lt;'</code> and <code>'&gt;'</code> instead of <code>'&lt;'</code> and <code>'&gt;'</code>
<code>import sys

n=int(input())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    if a&lt;b:
        print('&lt;')
    elif a&gt;b:
        print('&gt;')
    elif a==b:
        print('=')
</code>
