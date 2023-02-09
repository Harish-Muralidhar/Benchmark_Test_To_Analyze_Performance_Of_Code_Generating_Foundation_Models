'''

'''

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(n,m,arr):
    if m==1:
        return n
    if m==2:
        count=0
        for i in arr:
            if i%4==0:
                count+=1
        return count
    if m==3:
        count=0
        for i in arr:
            if i%8==0:
                count+=1
        return count
    if m==4:
        count=0
        for i in arr:
            if i%16==0:
                count+=1
        return count
    if m==5:
        count=0
        for i in arr:
            if i%32==0:
                count+=1
        return count
    if m==6:
        count=0
        for i in arr:
            if i%64==0:
                count+=1
        return count
    if m==7:
        count=0
        for i in arr:
            if i%128==0:
                count+=1
        return count
    if m==8:
        count=0
        for i in arr:
            if i%256==0:
                count+=1
        return count
    if m==9:
        count=0
        for i in arr:
            if i%512==0:
                count+=1
        return count
    if m==10:
        count=0
        for i in arr:
            if i%1024==0:
                count+=1
        return count
    if m==11:
        count=0
        for i in arr:
            if i%2048==0:
                count+=1
        return count
    if m==12:
        count=0
        for i in arr:
            if i%4096==0:
                count+=1
        return count
    if m==13:
        count=0
        for i in arr:
            if i%8192==0:
                count+=1
        return count
    if m==14