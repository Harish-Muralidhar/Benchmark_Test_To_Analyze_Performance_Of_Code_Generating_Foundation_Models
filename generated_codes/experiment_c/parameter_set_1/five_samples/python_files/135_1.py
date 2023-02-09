"""
For second query, 2 is connected to 3 by an edge. Hence distance 1.
For third query, 4 is at level 2 and 3 is at level 1. Hence distance 2+1=3

Solution:

def distance(i,j):
    dis = 0
    while i!=j:
        if i>j:
            i=i//2
        else:
            j=j//2
        dis+=1
    return dis

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        i,j = map(int,input().split(' '))
        print(distance(i,j))

"""