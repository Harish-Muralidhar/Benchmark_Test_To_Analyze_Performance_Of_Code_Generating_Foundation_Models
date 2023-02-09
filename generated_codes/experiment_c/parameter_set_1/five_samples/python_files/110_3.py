"""

"""


def hash_function(A,E,V,count=0,dp={}):
    """
    dp[(A,E,V)] = total strings
    """
    if (A,E,V) in dp:
        return dp[(A,E,V)]
    if V == 0:
        return 1
    if A == 0 and E == 0:
        return 0
    if A == 0 and E>0:
        return hash_function(A,E - 1,V,count)
    
    if E == 0 and A>0:
        return hash_function(A - 1,E,V-A,count)
        
    if A<=E:
        count+=hash_function(A,E-1,V,count)
        count+=hash_function(A-1,E,V-A,count)
    elif A>E:
        count+=hash_function(A,E-1,V,count)
        count+=hash_function(A-1,E,V-A,count)
    dp[(A,E,V)] = count
    return count
    
T = int(input())
for i in range(T):
    A,E,V = list(map(int,input().split()))
    print(hash_function(A,E,V)%1000000007)