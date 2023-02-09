'''

'''

# Write your code here

#input
number_of_test_cases = int(input())
#print(number_of_test_cases)

def count_min(s):
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    #print(r,g,b)
    if r == g and g == b:
        return 0
    elif r == g:
        return b
    elif r == b:
        return g
    elif g == b:
        return r
    else:
        return (r+g+b)
    
for i in range(number_of_test_cases):
    no_of_rooms = int(input())
    #print(no_of_rooms)
    s = input()
    #print(s)
    print(count_min(s))