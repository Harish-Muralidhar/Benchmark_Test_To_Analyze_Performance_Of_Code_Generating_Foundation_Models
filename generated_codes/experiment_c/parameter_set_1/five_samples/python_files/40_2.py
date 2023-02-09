"""
INDIAN

Explanation
First person described made 5 gestures, of which "Y" and "N" appear twice each. So, it is invalid. Second person is clearly from India. Third person made 6 gestures, of which "Y", "N" and "I" appear once each. So, he/she could be either Indian or not Indian. Fourth person is clearly not from India.

Sample Input
3
3 
YYY 
5 
NNNYY 
6 
NNINNI
Sample Output
INDIAN 
NOT INDIAN 
NOT SURE
"""

import sys

def get_input():
    return sys.stdin.readline().strip()

def get_input_int():
    return int(get_input())

def main():
    T = get_input_int()
    for _ in range(T):
        N = get_input_int()
        S = get_input()
        if N < 3 or (("Y" not in S or "N" not in S) and ("I" not in S or "N" not in S)):
            print("NOT SURE")
        elif "Y" in S or "I" in S:
            print("INDIAN")
        else:
            print("NOT INDIAN")

if __name__ == "__main__":
    main()