"""

For input:
3
100 2 1000000
100 3 1000000
100 4 1000000

the correct output is:
338350
2708167
22136850
"""

def sum_power_series(n,k,p):
    sum_s = 0
    for i in range(1,n+1):
        sum_s = sum_s + (i**k)%p
    print(sum_s%p)

#For taking the input
t = int(input())

for i in range(t):
    n,k,p = map(int,input().split())
    sum_power_series(n,k,p)