'''

Explanation

In the first case the favorite sequence is 2 3 4 and it is contained in the sequence 1 2 3 4 5 6

In the second case the favorite sequence is 4 15 and it is not contained in the sequence 22 5 6 33 1 4

'''

import itertools

def is_sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                    
                if n == len(s):
                    sub_set = True

    return sub_set

# Driver Code
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    s = list(map(int, input().split()))
    if is_sublist(l, s):
        print("Yes")
    else:
        print("No")