'''

Explanation

For the first test case, the atoms are {0,1,2}, {3} and {4}.

For the second test case, the atoms are {0}, {1}, {2} and {3}.

'''

# Write your code here
import sys

def get_input():
    input_str = sys.stdin.read()
    lines = input_str.split("\n")
    lines = lines[:-1]
    return lines

def get_test_cases(lines):
    test_cases = []
    i = 0
    while i < len(lines):
        n, m = lines[i].split(" ")
        n, m = int(n), int(m)
        test_case = []
        for j in range(m):
            v, s = lines[i+j+1].split(" ")
            v, s = int(v), [int(x) for x in s]
            test_case.append(s)
        test_cases.append(test_case)
        i += m+1
    return test_cases

def get_atoms(test_case):
    atoms = []
    for i in range(len(test_case)):
        for j in range(i+1, len(test_case)):
            atoms.append(list(set(test_case[i]) & set(test_case[j])))
    return atoms

def get_atoms_count(atoms):
    count = 0
    for atom in atoms:
        if len(atom) > 0:
            count += 1
    return count

def get_min_atoms(test_cases):
    min_atoms = []
    for test_case in test_cases:
        atoms = get_atoms(test_case)
        count = get_atoms_count(atoms)
        min_atoms.append(count)
    return min_atoms

def print_output(min_atoms):
    for min_atom in min_atoms:
        print(min_atom)

def main