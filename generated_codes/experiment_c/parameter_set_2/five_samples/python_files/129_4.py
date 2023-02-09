'''

Explanation

In the first test case, the atoms are {0,1,2}, {3}, and {4}.

In the second test case, the atoms are {0}, {1}, {2}, and {3}.

'''

#Solution

import sys

def find_atoms(n,m,arr):
    atoms = []
    for i in range(n):
        atoms.append(i)
    for i in range(m):
        for j in range(len(atoms)):
            if atoms[j] in arr[i]:
                atoms[j] = -1
    for i in range(len(atoms)):
        if atoms[i] == -1:
            atoms.remove(atoms[i])
            i -= 1
    return len(atoms)

t = int(sys.stdin.readline())
for i in range(t):
    n,m = map(int,sys.stdin.readline().split())
    arr = []
    for j in range(m):
        arr.append(list(map(int,sys.stdin.readline().split())))
    print(find_atoms(n,m,arr))