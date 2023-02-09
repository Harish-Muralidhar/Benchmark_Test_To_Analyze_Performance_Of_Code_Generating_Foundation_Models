"""



Solution:

"""

import sys
import numpy
import time

def getDiff(first, second):
    """
    get diff between two strings.
    diff = number of 'A' in first - number of 'A' in second
    return abs(diff)
    """
    a_first = first.count('A')
    a_second = second.count('A')
    return abs(a_first - a_second)

def getMin(first, second):
    """
    returns a string that is lexicographically less than first and second
    """
    if first < second:
        return first
    else:
        return second


def getMax(first, second):
    """
    returns a string that is lexicographically greater than first and second
    """
    if first < second:
        return second
    else:
        return first


def getPlacement(jack, jill):
    """
    Gets the placement of the objects based on the order
    jack and jill want to visit the locations.
    """
    placement = ''
    for i in range(len(jack)):
        if i % 2 == 0:
            placement += 'A'
        else:
            placement += 'B'

    return placement


def getFinalPlacement(jack, jill):
    """
    Gets the final placement of the objects based on the order
    jack and jill want to visit the locations.
    """
    jack_placement = getPlacement(jack, jill)
    jill_placement = getPlacement(jill, jack)
    #print "Jack placement: " + jack_placement
    #print "Jill placement: " + jill_placement

    if getDiff(jack_placement, jill_placement) <= 1:
        return getMin(jack_placement, jill_placement)
    else:
        return getMax(jack_placement, jill_placement)


def getOrder(order, placement):
    """
    returns a string of objects based on the locations
    """
    objects = ''
    for i in range(len(order)):
        objects += placement[order[i]]

    return objects


def main():
    """
    Main function.
    """
    test_cases = sys.stdin.readline()

    for i in range(int(test_cases)):
        size = sys.stdin.readline()
        jack = sys.stdin.readline().split()
        jill = sys.stdin.readline().split()

        jack_placement = getPlacement(jack, jill)
        jill_placement = getPlacement(jill, jack)

        #print "Jack placement: " + jack_placement
        #print "Jill placement: " + jill_placement

        jack_objects = getOrder(jack, jack_placement)
        jill_objects = getOrder(jill, jill_placement)
        #print "Jack objects: " + jack_objects
        #print "Jill objects: " + jill_objects

        if getDiff(jack_objects, jill_objects) <= 1:
            print getMin(jack_objects, jill_objects)
        else:
            print getMax(jack_objects, jill_objects)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))