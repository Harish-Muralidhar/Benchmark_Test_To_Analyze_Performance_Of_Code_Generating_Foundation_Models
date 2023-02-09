'''


Hint
To solve this question, you have to solve the queries offline.
This means that you have to preprocess the data.

You can preprocess the array using a prefix GCD array.
prefix_GCD[i] represents the GCD of elements from A[0] to A[i](inclusive).
prefix_GCD[i]=gcd(prefix_GCD[i-1], A[i]).

Say you have to answer a query G x y.
So for each element in the range [x,y](inclusive),
you have to check if GCD(G,A[i])>1. This is same as checking if GCD(G,prefix_GCD[i])>1.

Now, say you have to find the GCD(G,prefix_GCD[i]) for each i in the range [x,y](inclusive).
GCD(G,prefix_GCD[i])=GCD(G,prefix_GCD[y]/GCD(prefix_GCD[x-1],G))

So, you have to find the GCD(prefix_GCD[y],G) and GCD(prefix_GCD[x-1],G)

Now you can use the same logic to find the maximum element and its occurances in the set S.
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a = list(map(int, input().split()))

prefix_gcd = [0]
for i in range(1, n+1):
    prefix_gcd.append(gcd(prefix_gcd[i-1], a[i-1]))

for _ in range(m):
    g,x,y = map(int, input().split())
    gxy = gcd(prefix_gcd[y], g)
    gxm1 = gcd(prefix_gcd[x-1], g)

    if gxy==1:
        print('-1 -1')
        continue
    
    d = gxy//gxm1

    count = 0
    temp = d
    while temp<=gxy:
        if gcd(temp, gxy)==temp:
            count+=1
        temp+=d
    print(d, count)