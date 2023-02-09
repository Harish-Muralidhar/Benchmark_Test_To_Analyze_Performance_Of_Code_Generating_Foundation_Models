'''

Explanation
Example case 1.
There is no cell, which is a CPC. So there is no monster.
Example case 2.
The first cell is a CPC. It can accommodate 1 monster.
The third cell is a CPC, and it can accommodate 2 monsters.
The seventh cell is a CPC, and it can accommodate 1 monster.
Hence total monsters are 1 + 2 + 1.
'''



def is_prime(num):
    if num == 2:
        return True
    if num == 0 or num == 1 or num % 2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True

def L(arr,i,j,n,m):
    if arr[i][j] == '#' or arr[i][j] == '^':
        return 0
    count = 0
    while(j >= 0 and arr[i][j] == '^'):
        j -= 1
        count += 1
    return count

def R(arr,i,j,n,m):
    if arr[i][j] == '#' or arr[i][j] == '^':
        return 0
    count = 0
    while(j < m and arr[i][j] == '^'):
        j += 1
        count += 1
    return count

def T(arr,i,j,n,m):
    if arr[i][j] == '#' or arr[i][j] == '^':
        return 0
    count = 0
    while(i >= 0 and arr[i][j] == '^'):
        i -= 1
        count += 1
    return count

def B(arr,i,j,n,m):
    if arr[i][j] == '#' or arr[i][j] == '^':
        return 0
    count = 0
    while(i < n and arr[i][j] == '^'):
        i += 1
        count += 1
    return count

def check_prime(arr,i,j,n,m):
    if arr[i][j] == '#':
        return 0

    l=L(arr,i,j,n,m)
    r=R(arr,i,j,n,m)
    t=T(arr,i,j,n,m)
    b=B(arr,i,j,n,m)

    res=[]

    if l >= 2 and is_prime(l):
        res.append(l)

    if r >= 2 and is_prime(r):
        res.append(r)

    if t >= 2 and is_prime(t):
        res.append(t)

    if b >= 2 and is_prime(b):
        res.append(b)

    return len(res)

def count_monsters(arr,n,m):
    res=0
    for i in range(n):
        for j in range(m):
            res += check_prime(arr,i,j,n,m)
    return res

for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(input()))
    print(count_monsters(arr,n,m))