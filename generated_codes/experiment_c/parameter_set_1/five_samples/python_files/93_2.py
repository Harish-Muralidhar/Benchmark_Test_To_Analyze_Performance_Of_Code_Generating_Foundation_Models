'''
'''
from math import pow

def sumOfK(n,k,p):
    total = 0
    for i in range(1,n+1):
        total = total + pow(i,k)
    return (total%p)

def main():
    t = int(input())
    for i in range(t):
        n, k, p = map(int,input().split())
        print(int(sumOfK(n, k, p)))

if __name__ == "__main__":
    main()