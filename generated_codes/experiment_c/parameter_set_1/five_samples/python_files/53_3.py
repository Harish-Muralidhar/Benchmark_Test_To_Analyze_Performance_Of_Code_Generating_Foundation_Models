"""
 
 
 
 

"""
import sys

def get_palindrome_count(s):
    count = 0
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            count += 1
    return count

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    t = int(sys.stdin.readline().rstrip())

    while t > 0:
        n = int(sys.stdin.readline().rstrip())
        strings = []
        for i in range(n):
            s = sys.stdin.readline().rstrip()
            strings.append(s)
        print(get_palindrome_count(strings))

        t -= 1