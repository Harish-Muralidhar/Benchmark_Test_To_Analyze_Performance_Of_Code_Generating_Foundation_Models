'''

Explanation

Test Case 1:
1200 = 10 + 10 + 100 + 100 + 100 + 100 + 50 + 50 + 50 + 50 + 20 + 20

Test Case 2:
500 = 10 + 10 + 10 + 10 + 10 + 10 + 50 + 50 + 50 + 50 + 50

Test Case 3:
242 = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 10 + 10 + 10 + 10 + 10 + 10 + 100
'''

def currency(n):
    notes = [1,2,5,10,50,100]
    count = 0
    for i in range(len(notes)-1,-1,-1):
        if n >= notes[i]:
            count += n//notes[i]
            n = n%notes[i]
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(currency(n))