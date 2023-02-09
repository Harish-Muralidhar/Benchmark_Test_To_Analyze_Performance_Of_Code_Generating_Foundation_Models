'''


'''

# Write your code here
def ways(n):
    if n==1:
        return 1
    if n==2:
        return 5
    if n==3:
        return 11
    return ways(n-1)+5*ways(n-2)+ways(n-3)-ways(n-4)

t=int(input())
for i in range(t):
    n=int(input())
    print(ways(n)%1000000007)