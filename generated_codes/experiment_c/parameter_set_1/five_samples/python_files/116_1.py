"""


"""

def print_subarrays(arr, n): 
    for i in range(n): 
        for j in range(i, n): 
            for k in range(i, j + 1): 
                print(arr[k], end = " ") 
            print()
def get_subarrays(arr, n): 
    ans=[]
    for i in range(n): 
        for j in range(i, n): 
            l=[]
            for k in range(i, j + 1): 
                l.append(arr[k])
            ans.append(l)
    return ans
def get_subarrays1(arr, n): 
    ans=[]
    for i in range(n): 
        for j in range(i, n): 
            l=[]
            for k in range(i, j + 1): 
                l.append(arr[k])
            ans.append(l)
    return ans
              
    
def get_min_max(arr,start,end):
    if start == end:
        return arr[start],arr[start]
    elif start == end-1:
        if arr[start]>arr[end]:
            return arr[end],arr[start]
        else:
            return arr[start],arr[end]
    else:
        mid=(start+end)//2
        minl,maxl=get_min_max(arr,start,mid)
        minr,maxr=get_min_max(arr,mid+1,end)
        
    if minl<minr:
        minall=minl
    else:
        minall=minr
    if maxl>maxr:
        maxall=maxl
    else:
        maxall=maxr
    return minall,maxall
        
def get_min_max1(arr):
    minall=arr[0]
    maxall=arr[0]
    for i in arr:
        if minall > i:
            minall=i
        if maxall < i:
            maxall=i
    return minall,maxall

def get_all_subseq(arr,n):
    subs=get_subarrays(arr,n)
    minall,maxall=get_min_max(arr,0,n-1)
    all_subseq=[]
    for i in subs:
        all_subseq.append(i[:])
        minsub,maxsub=get_min_max(i,0,len(i)-1)
        #print(i,minsub,maxsub)
        if minsub != maxsub:
            all_subseq.append(i[:])
            if minsub>maxsub:
                minsub,maxsub=maxsub,minsub
            i[i.index(maxsub)]=maxsub-minsub
            all_subseq.append(i[:])
    return all_subseq

def cal1(arr,n):
    subs=get_subarrays(arr,n)
    ans=0
    for i in subs:
        s=set(i)
        if len(s)==1:
            ans+=1
    return ans

def cal2(arr,n):
    subs=get_subarrays(arr,n)
    ans=0
    for i in subs:
        if i[0]==1:
            ans+=1
    return ans

def cal3(arr):
    minall,maxall=get_min_max(arr,0,len(arr)-1)
    return minall