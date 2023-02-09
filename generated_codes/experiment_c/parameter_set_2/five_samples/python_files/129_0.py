'''

Explanation

In the first test case, we could partition X into the three sets {0,1,2}, {3}, and {4}.

In the second test case, we could partition X into the four sets {0}, {1}, {2}, and {3}.

'''

def get_atoms(n,m,S):
    # S is a list of sets
    atoms = []
    for i in range(n):
        # check if i is in any of the sets
        for s in S:
            if i in s:
                # if so, add it to the atoms list
                atoms.append(i)
                break
    return atoms

def main():
    t = int(input())
    for i in range(t):
        n,m = map(int, input().split())
        S = []
        for j in range(m):
            s = list(map(int, input().split()))
            S.append(set(s[1:]))
        atoms = get_atoms(n,m,S)
        print(len(atoms))

if __name__ == '__main__':
    main()