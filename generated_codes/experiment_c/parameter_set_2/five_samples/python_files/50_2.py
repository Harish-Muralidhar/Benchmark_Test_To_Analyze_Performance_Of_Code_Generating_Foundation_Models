"""


"""

def count_substrings(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1
    return count

print count_substrings("ABACABA")