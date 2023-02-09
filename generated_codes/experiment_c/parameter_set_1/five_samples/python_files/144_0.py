'''
'''
import math

#primes = [2,3]
#def is_prime(n):
#    global primes
#    if n in primes:
#        return True
#    limit = int(math.sqrt(n)+1)
#    for i in primes:
#        if i > limit:
#            primes.append(n)
#            return True
#        if n%i == 0:
#            return False
#    primes.append(n)
#    return True

#def prime_cross_cell(arr,i,j):
#    L = R = T = B = 0
#    for k in range(j-1,-1,-1):
#        if arr[i][k] == '#':
#            break
#        L += 1
#    for k in range(j+1,len(arr[0])):
#        if arr[i][k] == '#':
#            break
#        R += 1
#    for k in range(i-1,-1,-1):
#        if arr[k][j] == '#':
#            break
#        T += 1
#    for k in range(i+1,len(arr)):
#        if arr[k][j] == '#':
#            break
#        B += 1
#    m = min(L,R,T,B)
#    for p in primes:
#        if p > m:
#            return True
#    return False

def prime_cross_cell(arr,i,j):
    L = R = T = B = 0
    for k in range(j-1,-1,-1):
        if arr[i][k] == '#':
            break
        L += 1
    for k in range(j+1,len(arr[0])):
        if arr[i][k] == '#':
            break
        R += 1
    for k in range(i-1,-1,-1):
        if arr[k][j] == '#':
            break
        T += 1
    for k in range(i+1,len(arr)):
        if arr[k][j] == '#':
            break
        B += 1
    m = min(L,R,T,B)
    for p in range(2,m+1):
        if m%p == 0:
            return False
    return True

def main():
    t = int(input())
    while t:
        t -= 1
        r,c = map(int, input().split())
        arr = [input() for i in range(r)]
        count = 0
        for i in range(r):
            for j in range(c):
                if arr[i][j] == '^' and prime_cross_cell(arr,i,j):
                    count += 1
        print(count)

main()