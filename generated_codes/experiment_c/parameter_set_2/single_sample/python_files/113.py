"""
Example case 2. The first few fibonacci numbers are 0 , 1 , 1 , 2 , 3 ,5 , 8 , 13 and so on and the series is increasing . Only 3 and 5 appear in this series while 4 does not appear in the series . 
Example case 3. The first few fibonacci numbers are 0 , 1 , 1 , 2 , 3 ,5 , 8 , 13 and so on and the series is increasing . Only 3 and 5 appear in this series while 4 does not appear in the series . 

"""

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def check_fib(n):
    if n<=1:
        return "YES"
    else:
        i=0
        while True:
            if fib(i)==n:
                return "YES"
            elif fib(i)>n:
                return "NO"
            else:
                i+=1

t=int(input())
for i in range(t):
    n=int(input())
    print(check_fib(n))