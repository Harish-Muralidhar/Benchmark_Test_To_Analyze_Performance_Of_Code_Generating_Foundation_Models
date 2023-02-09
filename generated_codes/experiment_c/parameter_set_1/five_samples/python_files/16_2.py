'''


Solution:

'''

def gcd(a, b): 
      
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

def check(arr,n,k):
    g=arr[0]
    for i in range(1,n):
        g=gcd(g,arr[i])
        
    if(g%k==0):
        return True
    return False

def compute(arr,n,k):
    ops=0
    if(check(arr,n,k)):
        return 0
    else:
        #do the operations
        for i in range(n):
            while(arr[i]%k!=0):
                arr[i]+=1
                ops+=1
                
        return ops
                
        
        
        
        
        
        
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    print(compute(arr,N,K))