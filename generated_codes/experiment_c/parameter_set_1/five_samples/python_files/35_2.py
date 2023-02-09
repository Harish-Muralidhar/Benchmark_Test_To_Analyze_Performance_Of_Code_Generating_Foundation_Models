'''

'''
# Write code here 



##
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

n=int(input())
for i in range(n):
    no=int(input())
    print(factorial(no))