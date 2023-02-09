"""

"""

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

n = int(input())
for i in range(n):
    a = int(input())
    b = recur_fibo(a)
    if b == a:
        print("YES")
    else:
        print("NO")