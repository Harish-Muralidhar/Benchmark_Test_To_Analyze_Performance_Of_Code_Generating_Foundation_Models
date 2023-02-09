'''
'''

#python 3.x code
t = int(input())
while t:
    n = int(input())
    last = n % 10
    first = int(n / pow(10, len(str(n)) - 1))
    print(first + last)
    t = t - 1