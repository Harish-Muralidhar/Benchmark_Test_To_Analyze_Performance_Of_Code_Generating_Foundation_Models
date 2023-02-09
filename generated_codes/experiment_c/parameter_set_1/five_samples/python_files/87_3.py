'''

Input:
3
1 2 3
4 5 6
7 9 8

Output:
-1

Input:
2
1 2
2 1

Output:
1 2

Input:
3
1 2 3
2 3 1
3 1 2

Output:
2 3 1

'''

def crane(n):
    n1 = [int(x) for x in input().split()]
    n2 = [int(x) for x in input().split()]
    n3 = [int(x) for x in input().split()]


    if n1[0] < n2[0] and n1[0] < n3[0]:
        if n1[1] < n2[1] and n1[1] < n3[1]:
            print(1,2,3,sep=' ')
        elif n1[2] < n2[2] and n1[2] < n3[2]:
            print(1,3,2,sep=' ')
        else:
            print(-1)
            
    elif n2[0] < n1[0] and n2[0] < n3[0]:
        if n2[1] < n1[1] and n2[1] < n3[1]:
            print(2,3,1,sep=' ')
        elif n2[2] < n1[2] and n2[2] < n3[2]:
            print(2,1,3,sep=' ')
        else:
            print(-1)
    else:
        if n3[1] < n2[1] and n3[1] < n1[1]:
            print(3,2,1,sep=' ')
        elif n3[2] < n2[2] and n3[2] < n1[2]:
            print(3,1,2,sep=' ')
        else:
            print(-1)

n = int(input())
crane(n)