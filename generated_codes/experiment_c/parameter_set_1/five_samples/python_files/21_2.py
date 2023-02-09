'''

** For More Input/Output Examples Use 'Expected Output' option **
'''

# Write your code here
testCases = int(input())
for i in range(testCases):
    a,b = [int(i) for i in input().split()]
    print(a%b)