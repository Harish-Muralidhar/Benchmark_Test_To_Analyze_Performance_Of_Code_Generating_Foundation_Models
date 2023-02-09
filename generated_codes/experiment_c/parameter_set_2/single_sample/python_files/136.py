'''


'''

def nCr(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if r == 1:
        return n
    if r == 0:
        return 1
    if r == 2:
        return n*(n-1)//2
    if r == 3:
        return n*(n-1)*(n-2)//6
    if r == 4:
        return n*(n-1)*(n-2)*(n-3)//24
    if r == 5:
        return n*(n-1)*(n-2)*(n-3)*(n-4)//120
    if r == 6:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)//720
    if r == 7:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)//5040
    if r == 8:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)//40320
    if r == 9:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)//362880
    if r == 10:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)*(n-9)//3628800
    if r == 11:
        return n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8)*(n-9)*(n-10)//39916800
    if r == 12:
        return n*(n-1)*(n