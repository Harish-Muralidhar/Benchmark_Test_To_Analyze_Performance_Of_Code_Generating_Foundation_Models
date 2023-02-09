"""

"""

from sys import stdin,stdout
from math import *

def create_array(n,arr_list):
    arr = [0]*n

    for i in range(n):
        arr[i] = arr_list[i]

    return arr

def create_segtree(n,arr):
    tree = [0]*(2*n)

    for i in range(n,2*n):
        tree[i] = arr[i-n]

    for i in range(n-1,0,-1):
        tree[i] = min(tree[2*i],tree[2*i+1])

    return tree

def update(arr,tree,i,val,n):
    i = i + n - 1
    tree[i] = val

    while i!=1:
        tree[i//2] = min(tree[i],tree[i^1])
        i//=2

def query(tree,l,r,n):
    res = 9999999999
    l = l + n - 1
    r = r + n - 1

    while l<r:
        if l&1:
            res = min(res,tree[l])
            l += 1
        if r&1:
            res = min(res,tree[r-1])
        l//=2
        r//=2

    return res


def main():
    n,q = stdin.readline().split()
    n,q = int(n),int(q)

    arr_list = [int(x) for x in stdin.readline().split()]
    arr = create_array(n,arr_list)
    tree = create_segtree(n,arr)

    for i in range(q):
        query_list = [int(x) for x in stdin.readline().split()]
        if query_list[0]==0:
            stdout.write(str(query(tree,query_list[1],query_list[2],n))+"\n")
        else:
            for j in range(query_list[1],query_list[2]+1):
                arr[j-1] = arr[j-1]&query_list[3]
                update(arr,tree,j,arr[j-1],n)

if __name__ == '__main__':
    main()