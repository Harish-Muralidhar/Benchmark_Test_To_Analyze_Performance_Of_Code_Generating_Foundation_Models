'''
'''

def funfair(n,m,grid):
    #print(grid)
    if n==1 and m==1:
        return grid[0][0]
    elif n==1:
        return max(grid[0])
    elif m==1:
        return max([row[0] for row in grid])
    else:
        #print(grid)
        #print(n,m)
        if grid[0][0]==grid[0][m-1]==grid[n-1][0]==grid[n-1][m-1]:
            return grid[0][0]+funfair(n-1,m-1,[row[1:] for row in grid[1:]])
        elif grid[0][0]==grid[0][m-1]:
            return grid[0][0]+funfair(n-1,m-1,[row[1:] for row in grid[1:]])
        elif grid[0][0]==grid[n-1][0]:
            return grid[0][0]+funfair(n-1,m-1,[row[1:] for row in grid[1:]])
        elif grid[0][0]==grid[n-1][m-1]:
            return grid[0][0]+funfair(n-1,m-1,[row[1:] for row in grid[1:]])
        elif grid[0][m-1]==grid[n-1][0]:
            return grid[0][m-1]+funfair(n-1,m-1,[row[:-1] for row in grid[1:]])
        elif grid[0][m-1]==grid[n-1][m-1]:
            return grid[0][m-1]+funfair(n-1,m-1,[row[:-1] for row in grid[1:]])
        elif grid[n-1][0]==grid[n-1][m-1]:
            return grid[n-1][0]+funfair(n-1,m-1,[row[:-1] for row in grid