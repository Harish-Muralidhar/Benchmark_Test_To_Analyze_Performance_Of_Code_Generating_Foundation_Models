'''

Explanation

In the first test case, the optimal solution is to create the three sets {0,1}, {2,3} and {4}.

In the second test case, the optimal solution is to create the four sets {0}, {1}, {2} and {3}.

'''

def find_atoms(n, m, sets):
    atoms = []
    for i in range(n):
        atoms.append(set([i]))
    for s in sets:
        for atom in atoms:
            if len(atom & s) == 0:
                atom |= s
                break
    return len(atoms)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        sets = []
        for _ in range(m):
            s = set(map(int, input().split()[1:]))
            sets.append(s)
        print(find_atoms(n, m, sets))