'''
 = 90, n = 2, n = 2. Note that it's not sufficient to know the number of Johnny's lies, but we also need to know the exact number of lies, because the number of lies is needed to determine the exact answer to Alice's question.

Please use as few lines of code as possible, but note that your solution should still be readable.


'''

import sys

def main():
    assert len(sys.argv) == 2, "Usage: python guessing.py input_file"
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        t = int(f.readline())
        assert 1 <= t <= 20
        for i in range(t):
            k = int(f.readline())
            assert 1 <= k <= 100000
            guesses = []
            for j in range(k):
                line = f.readline()
                line = line.split()
                assert len(line) == 3
                operator = line[0]
                li = int(line[1])
                assert 1 <= li <= 10**9
                logical_value = line[2]
                assert logical_value in ["Yes", "No"]
                guesses.append((operator, li, logical_value))
            print(count_lies(guesses))

def count_lies(guesses):
    '''Return the minimal number of lies in Johnny's guesses.'''
    # TODO: implement me
    return 0

if __name__ == "__main__":
    main()