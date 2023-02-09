'''

'''

import math

def isPrime(n):
    if(n==1):
        return False
    if(n==2):
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return True

def countMonster(arr,i,j):
    ctr=0
    for p in range(1,min(i+1,len(arr[0])-j,len(arr)-i)+1):
        l=0
        r=0
        t=0
        b=0
        for k in range(j):
            if(arr[i][k]=='^'):
                l+=1
            else:
                break
        for k in range(j+1,len(arr[0])):
            if(arr[i][k]=='^'):
                r+=1
            else:
                break

        for k in range(i):
            if(arr[k][j]=='^'):
                t+=1
            else:
                break
        for k in range(i+1,len(arr)):
            if(arr[k][j]=='^'):
                b+=1
            else:
                break
        if(isPrime(p) and min(l,r,t,b)>=p):
            ctr+=1
    return ctr

def main():
    t=int(input())
    for i in range(t):
        r,c=list(map(int,input().split()))
        arr=[]
        for i in range(r):
            arr.append(input())
        ctr=0
        for i in range(r):
            for j in range(c):
                if(arr[i][j]=='^'):
                    ctr+=countMonster(arr,i,j)
        print(ctr)

if __name__=='__main__':
    main()