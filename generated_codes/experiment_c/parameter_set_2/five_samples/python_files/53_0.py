'''

'''

def isPalindrome(s):
    return s == s[::-1]

def isPalindrome2(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def isPalindrome3(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome4(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome5(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome6(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome7(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome8(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome9(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome10(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome11(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome12(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def isPalindrome13(s):
    return all(s[i] == s[~i] for i in range(len(