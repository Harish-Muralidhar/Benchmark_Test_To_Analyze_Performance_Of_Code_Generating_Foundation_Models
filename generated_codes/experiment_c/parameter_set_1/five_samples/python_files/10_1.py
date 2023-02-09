'''

Test Case Generation
The first line of the input contains the number of test-cases T. T test cases follow. Each test case is generated as follows:

The number of streets N is chosen uniformly between 1 and 100000.
The value K is chosen uniformly between 1 and N.
The special numbers of streets are chosen uniformly between 1 and 100000.

'''

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    prod=1
    for i in range(n):
        prod*=a[i]
    print(prod)