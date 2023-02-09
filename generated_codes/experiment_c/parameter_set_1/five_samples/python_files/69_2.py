'''

'''



def findGCD(a, b): 
      
    if(b == 0): 
        return a 
    else: 
        return findGCD(b, a % b) 
  
def gcd_query(g, a, n): 
      
    res = 0
    for i in range(n): 
  
        if(findGCD(g, a[i]) > 1): 
          
            res += 1
  
    return res 
  
n, m = list(map(int, input().split() )) 
a = list(map(int, input().split() )) 
  
# take the query 
for _ in range(m): 
    g, x, y = list(map(int, input().split() )) 
    x, y = x-1, y-1
    if(gcd_query(g, a[x:y+1], n) > 0): 
        print(max(a[x:y+1]), gcd_query(max(a[x:y+1]), a[x:y+1], n)) 
    else: 
        print(-1, -1)