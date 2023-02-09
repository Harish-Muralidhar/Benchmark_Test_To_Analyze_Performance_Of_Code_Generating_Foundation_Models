'''



'''

def findProgression(L,R,k,n):
    # Write your code here
    step = k
    total = 0
    lenght = 1
    list_of_set = []
    for i in range(L,R+1):
        if i+step <= R:
            list_of_set.append([i,i+step])
            total += 1
        step += k
    
    
    
    
    
    
    
    
    
    
    
    
    return total,list_of_set

if __name__ == "__main__":
    L,R,k,n = map(int,input().split())
    result = findProgression(L,R,k,n)
    print(result)