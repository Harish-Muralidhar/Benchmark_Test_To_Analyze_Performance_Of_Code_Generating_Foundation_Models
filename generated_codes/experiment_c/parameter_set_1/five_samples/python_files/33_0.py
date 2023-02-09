'''

'''

# Write the code here



def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a*b) // gcd(a, b)

for i in range(int(input())):
    a, b = map(int, input().split())
    print(gcd(a, b), lcm(a, b))