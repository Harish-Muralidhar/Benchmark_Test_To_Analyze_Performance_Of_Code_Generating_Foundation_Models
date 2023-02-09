"""


"""

import sys
import itertools

def main():
    num_of_test_cases = int(sys.stdin.readline().strip())
    for i in range(num_of_test_cases):
        n = int(sys.stdin.readline().strip())
        jack_order = [int(x) for x in sys.stdin.readline().strip().split()]
        jill_order = [int(x) for x in sys.stdin.readline().strip().split()]
        print(find_optimal_placement(n, jack_order, jill_order))

def find_optimal_placement(n, jack_order, jill_order):
    # Create a list of all possible placements
    placements = list(itertools.product(['A', 'B'], repeat=n))
    # Create a list of all possible differences for each placement
    differences = []
    for placement in placements:
        differences.append(get_differences(placement, jack_order, jill_order))
    # Find the minimum difference
    min_difference = min(differences)
    # Find all placements with the minimum difference
    min_placements = [placement for placement, difference in zip(placements, differences) if difference == min_difference]
    # Return the lexicographically least placement
    return min(min_placements)

def get_differences(placement, jack_order, jill_order):
    # Create a list of all possible differences for each placement
    jack_differences = []
    jill_differences = []
    for i in range(len(placement)):
        jack_differences.append(get_difference(placement, jack_order, i))
        jill_differences.append(get_difference(placement, jill_order, i))
    # Return the maximum difference
    return max(max(jack_differences), max(jill_differences))

def get_difference(placement, order, t):
    # Create a list of the first t items in