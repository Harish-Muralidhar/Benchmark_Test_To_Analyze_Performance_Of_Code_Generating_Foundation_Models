'''

Input:
2
8 3
3 0 1 2
3 2 3 4
3 4 5 6
8 2
3 0 1 2
3 2 3 4

Output:
4
4

Explanation:

Test Case 1: The partition {0, 1, 2}, {3, 4}, {5, 6} is a valid partition into 3 atoms.

Test Case 2: The partition {0, 1, 2}, {3, 4}, {5, 6}, {7} is a valid partition into 4 atoms.

Test Case 3: The partition {0, 1, 2}, {3, 4}, {5, 6}, {7} is a valid partition into 4 atoms.

Your code should be able to process the input file in under 5 seconds.

Hint: Consider using a set of subsets that contains every possible subset of X.

'''


def subsetOf(A, B):
    for x in A:
        if x not in B:
            return False
    return True

def commonSubset(A, B):
    for x in A:
        if x in B:
            return True
    return False

def atom(A, Si):
    for i in range(len(Si)):
        if subsetOf(A, Si[i]):
            return False
    return True

def atom2(A, Si):
    for i in range(len(Si)):
        if commonSubset(A, Si[i]):
            return False
    return True

def partition(X, Si):
    A = []
    for x in X:
        if atom2([x], Si):
            A.append([x])
    return A

def partition2(X, Si):
    A = []
    while True:
        if not X:
            break
        for i in range(1, len(X) + 1):
            if atom2(X[0:i], Si):
                #print(X[0:i])
                A.append(X[0:i])
                X = X[i:]
                break
    return A

def main():
    f = open('input.txt', 'r')
    n = int(f.readline())
    for i in range(n):
        x = f.readline()
        x = x.split()
        #print(x)
        n = int(x[0])
        m = int(x[1])
        Si = []
        for j in range(m):
            x = f.readline()
            x = x.split()
            x[0] = int(x[0])
            x[1:] = [int(y) for y in x[1:]]
            Si.append(x[1:])
        #print(n, m, Si)
        X = [i for i in range(n)]
        #print(X)
        A = partition2(X, Si)
        print(len(A))

if __name__ == "__main__":
    main()