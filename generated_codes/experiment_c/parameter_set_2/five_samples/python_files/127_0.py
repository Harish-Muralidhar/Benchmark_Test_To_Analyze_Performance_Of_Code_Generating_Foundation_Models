'''

'''

# Write your code here

def winner(s,dictionary):
    if s in dictionary:
        return 'Tracy'
    else:
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j] in dictionary:
                    return winner(s[:i]+s[j:],dictionary)
    return 'Teddy'

t = int(input())
for _ in range(t):
    s = input()
    n = int(input())
    dictionary = []
    for i in range(n):
        dictionary.append(input())
    print(winner(s,dictionary))