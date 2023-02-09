'''

2.
Write a python code for the following question.
Import the necessary libraries.

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

'''
# A Dynamic Programming based Python3 program to find length
# of the longest common substring
def lcs(X, Y, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
    print(L)
    # Following steps build L[m + 1][n + 1] in bottom up fashion.
    # Note that L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following code is used to print LCS
    index = L[m][n]

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS of " + X + " and " + Y + " is " + "".join(lcs))

    return L[m][n]


# Driver program to test the above function
X = "abdc"
Y = "bacb"
m = len(X)
n = len(Y)
lcs(X, Y, m, n)

# This code is contributed by BHAVYA JAIN

class Solution:
    def almostIncreasingSequence(self, sequence):
        drop = 0
        for i in range(1, len(sequence)):
            if sequence[i] <= sequence[i - 1]:
                drop += 1
                if drop > 1:
                    return False
                if i - 2 < 0 or sequence[i] > sequence[i - 2]:
                    sequence[i - 1] = sequence[i]
                else:
                    sequence[i] = sequence[i - 1]
        return True


sequence = [1, 3, 2, 1]
print(Solution().almostIncreasingSequence(sequence))