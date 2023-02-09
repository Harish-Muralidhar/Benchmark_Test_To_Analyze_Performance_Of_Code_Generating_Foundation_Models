'''

'''

#code

t = int(input())

for i in range(t):
    n = int(input())
    c = 0
    while n>0:
        c = c + n
        n = n-1
    print(c)