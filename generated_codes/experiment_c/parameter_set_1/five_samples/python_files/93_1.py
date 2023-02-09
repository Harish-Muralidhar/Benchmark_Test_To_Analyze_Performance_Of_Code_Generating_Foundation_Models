'''

'''
# define a function which will take input as n,k,p
def find_modulo(n,k,p):
    # initialise a sum = 0
    sum = 0
    # run a for loop from 1 to n
    for i in range(1,n+1):
        # calculate i^k and append it to the sum
        sum += (i**k)
        # take the mod of the sum with p to avoid overflow
        sum = sum%p
    return sum

# initialise a count = 0
count = 0
# take the input from the user
t = int(input())
while count < t:
    n,k,p = map(int, input().split())
    # call the function and print the output
    print(find_modulo(n,k,p))
    count += 1