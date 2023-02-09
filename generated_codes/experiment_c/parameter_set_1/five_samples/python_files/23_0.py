'''

Explanation

Test Case 1:
12 ten rupee notes

Test Case 2:
5 hundred rupee notes

Test Case 3:
1 hundred rupee note, 1 ten rupee note, 1 two rupee note and 2 one rupee note.
'''

import sys
import math

def main(args):
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_currency(n))

def count_currency(n):
    notes = [1, 2, 5, 10, 50, 100]
    count = 0
    for i in range(len(notes) - 1, -1, -1):
        count += n // notes[i]
        n = n % notes[i]
    return count

if __name__ == "__main__":
    main(sys.argv)