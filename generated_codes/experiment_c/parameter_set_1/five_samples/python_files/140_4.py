
# In[1]:


from datetime import datetime
start_time = datetime.now()
from math import factorial
from math import pow
import sys
t=int(input())
while(t>0):
    n=int(input())
    c=0
    for i in range(n//2-1,n+1):
        if(((n+i)%2==0)and(n!=2)):
            c+=int((factorial(n+i)/(factorial(i)*factorial(n-i+2)))%(pow(10,9)+7))
        elif(((n+i)%2==0)and(n==2)):
            c=int(5%(pow(10,9)+7))
    print(c)
    t-=1
print(datetime.now()-start_time)


# In[ ]: