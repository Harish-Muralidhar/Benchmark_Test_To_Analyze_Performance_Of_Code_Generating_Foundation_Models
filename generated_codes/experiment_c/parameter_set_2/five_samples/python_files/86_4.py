'''


'''

#code
import sys
sys.setrecursionlimit(1500)

def find_path(x,y,n,m,mat,visited,count):
    if x==n-1 and y==m-1:
        count[0]+=1
        return
    visited[x][y]=1
    mat[x][y]-=1
    if x+1<n and mat[x+1][y]>0 and visited[x+1][y]==0:
        find_path(x+1,y,n,m,mat,visited,count)
    if x+2<n and mat[x+2][y]>0 and visited[x+2][y]==0:
        find_path(x+2,y,n,m,mat,visited,count)
    if x-1>=0 and mat[x-1][y]>0 and visited[x-1][y]==0:
        find_path(x-1,y,n,m,mat,visited,count)
    if x-2>=0 and mat[x-2][y]>0 and visited[x-2][y]==0:
        find_path(x-2,y,n,m,mat,visited,count)
    if y+1<m and mat[x][y+1]>0 and visited[x][y+1]==0:
        find_path(x,y+1,n,m,mat,visited,count)
    if y+2<m and mat[x][y+2]>0 and visited[x][y+2]==0:
        find_path(x,y+2,n,m,mat,visited,count)
    if y-1>=0 and mat[x][y-1]>0 and visited[x][y-1]==0:
        find_path(x,y-1,n,m,mat,visited,count)
    if y-2>=0 and mat[x][y-2]>0 and visited[x][y-2]==0