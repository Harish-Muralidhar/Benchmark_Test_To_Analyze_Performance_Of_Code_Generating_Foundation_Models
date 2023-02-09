"""

Explanation:

In the first test case the favorite sequence is 2 3 4 and it is contained in the given sequence.
In the second test case the favorite sequence is 4 15 but it is not contained in the given sequence.

"""

# Write your code here

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    if b in a:
        print("Yes")
    else:
        print("No")