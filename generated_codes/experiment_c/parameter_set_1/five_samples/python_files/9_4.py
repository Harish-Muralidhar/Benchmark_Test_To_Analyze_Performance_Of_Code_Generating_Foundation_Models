'''

Sample Explanation
In the first case the moves are:

S1="CHEFCHEFFF" -> "CHFFF" -> "FFF"
S2="CHEFCHEFFFF" -> "CHFFFF" -> "FFFF"

In the second case there is no move.

'''

# Write your code here
s = input()

def substr(string, start, end): 
    return string[start:end] 

def find_all(string, sub):
    l = []
    start = 0
    while True:
        start = string.find(sub, start)
        if start == -1: return l
        l.append(start)
        start += len(sub) # use start += 1 to find overlapping matches
    return l

def count_chef(string):
    # 'CHEF'
    count = 0
    index_list = find_all(string, 'CHEF')
    for i in index_list:
        s = substr(string, 0, i)
        s = s + substr(string, i+4, len(string))
        count = max(count, count_chef(s))
    
    return count + 1
        

print(count_chef(s) - 1)