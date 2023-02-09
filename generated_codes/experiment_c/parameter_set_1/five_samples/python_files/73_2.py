"""

Explanation

Example case 1: When played at the same time, the notations (2, 5, 8, 11) and (2, 4, 8, 16) form the Arigeom beat notation (2, 4, 5, 8, 11, 16).
Example case 2: When played at the same time, the notations (2, 3, 4, 5) and (1, 2, 4, 5) form the Arigeom beat notation (1, 2, 3, 4, 5).
Example case 3: When played at the same time, the notations (2, 4, 8, 16) and (1, 2, 4, 8) form the Arigeom beat notation (1, 2, 4, 8, 16).
Example case 4: When played at the same time, the notations (2, 3, 9, 10, 19, 27) and (1, 2, 8, 10, 27, 28) form the Arigeom beat notation (1, 2, 3, 8, 9, 10, 19, 27, 28)."""



T=int(input())
while T:
    T=T-1
    n=int(input())
    arr=input().split(' ')
    for i in range(n):
        arr[i]=int(arr[i])
    i=0
    j=1
    diff1=arr[i+1]-arr[i]
    flag=0
    while j<n:
        diff2=arr[j]-arr[j-1]
        if diff2!=diff1:
            flag=1
            break
        j=j+1
    if flag:
        if diff1>diff2:
            print(arr[0],end=' ')
            i=1
            while i<j:
                print(arr[i],end=' ')
                i=i+1
            print()
            diff=arr[i]/arr[i-1]
            print(arr[i],end=' ')
            i=i+1
            while i<n:
                print(int(arr[i-1]*diff),end=' ')
                i=i+1
        else:
            print(arr[0],end=' ')
            i=1
            while i<j:
                print(arr[i],end=' ')
                i=i+1
            print()
            diff=arr[i]/arr[i-1]
            print(arr[i],end=' ')
            i=i+1
            while i<n:
                print(int(arr[i-1]*diff),end=' ')
                i=i+1
    else:
        while i<n:
            print(arr[i],end=' ')
            i=i+1
        print()
        i=0
        diff=arr[i+1]/arr[i]
        print(arr[i],end=' ')
        i=i+1
        while i<n:
            print(int(arr[i-1]*diff),end=' ')
            i=i+1
    print()