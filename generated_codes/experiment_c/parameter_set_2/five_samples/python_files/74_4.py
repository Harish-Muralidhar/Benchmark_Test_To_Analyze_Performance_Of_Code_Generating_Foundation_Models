'''

Explanation

In the first test case the longest progression is 2, 4, 6. In the second test case there are no such progressions. In the third test case the longest progression is 5, 9, 13, 17.

Constraints

1 <= T <= 10000
1 <= L <= R <= 10^9
1 <= k <= R - L
1 <= n <= 10^18

'''

import math

def find_longest_progression(L, R, k):
    #find the longest progression
    #the longest progression is the one with the most numbers
    #the number of numbers in the progression is (R-L)/k
    #the first number in the progression is L
    #the last number in the progression is R
    #the progression is L, L+k, L+2k, L+3k, ..., R
    #the number of progressions is (R-L)/k - 1
    #the last number in the progression is R
    #the first number in the progression is L
    #the progression is L, L+k, L+2k, L+3k, ..., R
    #the number of progressions is (R-L)/k - 1
    number_of_numbers = (R-L)/k
    number_of_progressions = number_of_numbers - 1
    return number_of_progressions

def find_first_two_terms(L, R, k, n):
    #find the first two terms of the nth progression
    #the first two terms of the nth progression are the first two terms of the nth progression
    #the first two terms of the nth progression are the first two terms of the nth progression
    #the first two terms of the nth progression are the first two terms of the nth progression
    #the first two terms of the nth progression are the first two terms of the nth progression
    #the first two terms of the nth progression are the first two terms of the nth progression
    #the first two terms of the nth progression are the first two terms of the nth progression
    #the first two terms of the nth progression are the first two