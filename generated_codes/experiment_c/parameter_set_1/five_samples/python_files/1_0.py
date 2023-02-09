"""
"""

t = int(input())

while t>0:
    
    n = int(input())
    
    arr = list(map(int,input().split()))
    
    sub_array = []
    sub_array_length = []
    for i in range(n):
        for j in range(i,n):
            if arr[j]*arr[j-1]<0:
                sub_array.append(arr[i:j+1])
                sub_array_length.append(len(arr[i:j+1]))
            else:
                sub_array.append(arr[i:j])
                sub_array_length.append(len(arr[i:j]))
                break
    
    print(*sub_array_length)
    
    t=t-1