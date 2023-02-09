"""
"""
#program
import math
def bico(r,c,g):
    output=[]
    while(g>0):
        if(r>0):
            if(r>=c):
                if(g>=math.factorial(r)//(math.factorial(c)*math.factorial(r-c))):
                    output.append(math.factorial(r)//(math.factorial(c)*math.factorial(r-c)))
                    g-=math.factorial(r)//(math.factorial(c)*math.factorial(r-c))
                    r-=1
                    c-=1
                else:
                    r-=1
                    c-=1
            else:
                if(g>=math.factorial(r)//(math.factorial(c)*math.factorial(r-c))):
                    output.append(math.factorial(r)//(math.factorial(c)*math.factorial(r-c)))
                    g-=math.factorial(r)//(math.factorial(c)*math.factorial(r-c))
                    r-=1
                    c-=1
                else:
                    r-=1
                    c-=1
        else:
            break
    return output

t=int(input())
for _ in range(t):
    r,c,g=map(int,input().split())
    g=g-(r*(r+1)//2)
    output=bico(r,c,g)
    print(len(output))
    print(" ".join(map(str,output)))