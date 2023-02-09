"""

*/

import sys

def readin(line):
    """
    Convert a line of input into a tuple of the form [(jill, jack)]
    """
    junk, jill, jack = line.split()
    return (jill, jack)

def count_diffs(permutations):
    """
    Return the max count of differences between the jill and jack lists
    """
    max_diffs = 0
    for jill, jack in permutations:
        diff = 0 #keep a running total of the difference between the two lists
        for idx in range(len(jill)):
            if jill[idx] < jack[idx]:
                diff += 1
            else:
                diff -= 1
            max_diffs = max(max_diffs, abs(diff))
    return max_diffs

def get_permutations(jill, jack):
    """
    Return a list of all permutations of jill and jack
    """
    ret = []
    for idx in range(len(jill)):
        ret.append((jill[idx:] + jill[:idx], jack[idx:] + jack[:idx]))
    return ret

def get_index(index, permutation):
    """
    Return the element at index given the current permutation
    """
    return permutation[index]

def solve(permutations):
    """
    Return a string where each character represents an item in a list.
    """
    #Get the max_diffs to beat
    min_diffs = count_diffs(permutations)
    #Create the list of items
    items = ['A' for i in range(min_diffs)]
    items.extend(['B' for i in range(min_diffs)])
    #Search all possible combinations
    for perm in permutations:
        print_list = []
        for idx in range(len(items)):
            print_list.append(items[get_index(idx, perm[0])])
        print "".join(print_list)
        return  # only return the first one

def main(filename):
    """
    Read in a file containing the input data and print the output
    """
    fp = open(filename, 'r')
    num_tests = int(fp.readline())
    for i in range(num_tests):
        num_permutations = int(fp.readline())
        jill = fp.readline()
        jack = fp.readline()
        solve(get_permutations(jill, jack))

if __name__ == '__main__':
    main(sys.argv[1])