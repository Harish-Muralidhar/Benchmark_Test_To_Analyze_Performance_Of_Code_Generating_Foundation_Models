'''

'''

#Solution

def prime_words(a,b):
    if a == b:
        return (a+1)*(b+1)//2
    else:
        return (a+1)*(b+1)

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print(prime_words(a,b)%531169)