'''

'''

#code

def currency_notes(n):
    notes = [1, 2, 5, 10, 50, 100]
    count = 0
    for i in range(len(notes)-1, -1, -1):
        count += n//notes[i]
        n = n%notes[i]
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(currency_notes(n))