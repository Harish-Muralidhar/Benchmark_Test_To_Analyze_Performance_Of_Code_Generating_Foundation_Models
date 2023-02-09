"""

Explanation

In the first test case, the atoms are {0,1,2}, {3}, and {4}.

In the second test case, the atoms are {0}, {1}, {2}, and {3}.

"""

import sys

def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    return lines

def process_input(lines):
    t = int(lines[0])
    test_cases = []
    for i in range(t):
        n, m = [int(x) for x in lines[1].split()]
        test_cases.append(lines[2:2+m])
        lines = lines[2+m:]
    return test_cases

def find_atoms(test_cases):
    atoms = []
    for test_case in test_cases:
        atoms.append(find_atoms_for_test_case(test_case))
    return atoms

def find_atoms_for_test_case(test_case):
    atoms = []
    for line in test_case:
        atoms = find_atoms_for_line(atoms, line)
    return atoms

def find_atoms_for_line(atoms, line):
    if not atoms:
        atoms = [set(line[1:])]
    else:
        new_atoms = []
        for atom in atoms:
            new_atoms += find_atoms_for_atom(atom, line)
        atoms = new_atoms
    return atoms

def find_atoms_for_atom(atom, line):
    new_atoms = []
    for number in line[1:]:
        if number in atom:
            new_atom = atom.copy()
            new_atom.remove(number)
            new_atoms.append(new_atom)
            atom.remove(number)
    if atom:
        new_atoms.append(atom)
    return new_atoms

def print_output(atoms):
    for atom in atoms:
        print