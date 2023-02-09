'''

'''

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
    
    
def minimum_deletions(lst):
    count = 0
    for i in range(len(lst)):
        if isPalindrome(lst[i]):
            count = count + 1
    return (len(lst) - count)
    
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(str, input().split()))
    res = minimum_deletions(lst)
    print (res)