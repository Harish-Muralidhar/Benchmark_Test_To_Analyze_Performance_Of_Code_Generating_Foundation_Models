"""

"""

def find_subarray(n,e,o):
    if e+o != n*(n+1)/2:
        return -1
    if e%2 == 1:
        return -1
    if e == 0:
        return [2]*n
    if e == n*(n+1)/2:
        return [1]*n
    if e == n:
        return [2]*n
    if e == n-1:
        return [2]*(n-1)+[1]
    if e == n-2:
        return [2]*(n-2)+[1,1]
    if e == n-3:
        return [2]*(n-3)+[1,1,1]
    if e == n-4:
        return [2]*(n-4)+[1,1,1,1]
    if e == n-5:
        return [2]*(n-5)+[1,1,1,1,1]
    if e == n-6:
        return [2]*(n-6)+[1,1,1,1,1,1]
    if e == n-7:
        return [2]*(n-7)+[1,1,1,1,1,1,1]
    if e == n-8:
        return [2]*(n-8)+[1,1,1,1,1,1,1,1]
    if e == n-9:
        return [2]*(n-9)+[1,1,1,1,1,1,1,1,1]
    if e == n-10:
        return [2]*(n-10)+[1,1,1,1,1,1,1,1,1,1]
    if e == n-11:
        return [2]*(n-11)+[1,1,1,1,1,1,1,1,1,1,1]
    if e == n-12:
        return [2]*(n-12)+[