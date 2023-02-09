'''


Input:
1
3
0 0 0
1 1 0
1 1 0
1 1 0
1 1 1
0 0 0

Output:
-1

'''
#Solution:

def operate1(i,j,grid):
    for k in range(len(grid)):
        if(grid[i][k]==0):
            grid[i][k]=1
        else:
            grid[i][k]=0
    for k in range(len(grid)):
        if(grid[k][j]==0):
            grid[k][j]=1
        else:
            grid[k][j]=0
    return grid
def check(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j]!=final[i][j]):
                return False
    return True
def operate(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid1=grid.copy()
            grid1=operate1(i,j,grid1)
            if(check(grid1)):
                return [i,j]
    return [None,None]
t=int(input())
for _ in range(t):
    n=int(input())
    grid=[]
    for _ in range(n):
        row=list(map(int,input().split()))
        grid.append(row)
    final=[]
    for _ in range(n):
        row=list(map(int,input().split()))
        final.append(row)
    flag=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j]!=final[i][j]):
                flag=1
                break
        if(flag==1):
            break
    if(flag==0):
        print('0')
    else:
        ans=operate(grid)
        if(ans[0]==None):
            print('-1')
        else:
            print(ans[1]+1)
            print(ans[0]+1)