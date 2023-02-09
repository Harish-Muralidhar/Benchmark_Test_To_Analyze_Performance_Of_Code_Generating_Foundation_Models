'''

Time Limit: 1 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: C, CPP, CLOJURE, CSHARP, D, ERLANG, FSHARP, GO, GROOVY, HASKELL, JAVA, JAVA8, JAVASCRIPT, JAVASCRIPT_NODE, LISP, LISP_SBCL, LUA, OBJECTIVEC, OCTAVE, PASCAL, PERL, PHP, PYTHON, R, RACKET, RUBY, RUST, SCALA, SWIFT, VB

 
'''


def is_good_number(string):
    dp = [0]*len(string)
    if string[0] == '.':
        dp[0] = 1
    if string[1] == '.':
        dp[1] = dp[0]
    for i in range(2, len(string)):
        if string[i] == '.':
            dp[i] = dp[i-2] + dp[i-1]
    return dp[-1]


# there are multiple ways of doing this
# for example, like this one (I'm using it for my own solution)
def is_good_number(string):
    dp = [0]*len(string)
    if string[0] == '.':
        dp[0] = 1
    if string[1] == '.':
        dp[1] = dp[0]
    for i in range(2, len(string)):
        if string[i] == '.':
            dp[i] = dp[i-2] + dp[i-1]
    return dp[-1]


def get_good_number(L, R, N):
    if L > R:
        return -1
    for i in range(L, R+1):
        if is_good_number(bin(i)[2:]) == N:
            return i
    return -1


# import sys
# sys.stdin = open('input.in', 'r')
# sys.stdout = open('output.out', 'w')

T = int(input())

for _ in range(T):
    l, r, n = [int(x) for x in input().strip().split()]
    print(get_good_number(l, r, n), bin(get_good_number(l, r, n))[2:])

'''
In the code above, I've used binary representation of numbers, which reduces the problem to O(r-l).

I modified the code slightly for the submission, I've replaced the is_good_number function with another one, that doesn't use binary numbers, but instead uses string representation of numbers.
'''