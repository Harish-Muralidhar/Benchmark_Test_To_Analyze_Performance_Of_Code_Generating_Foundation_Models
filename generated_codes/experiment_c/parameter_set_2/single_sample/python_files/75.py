'''

'''

import itertools

def is_possible(n,k,a):
    for i in range(1,n):
        for subset in itertools.combinations(a,i):
            if sum(subset) == (n-1)*k:
                return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        if is_possible(n,k,a):
            print('YES')
        else:
            print('NO')

main()