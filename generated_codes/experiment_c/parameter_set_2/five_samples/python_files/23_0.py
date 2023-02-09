'''

Explanation

Test Case 1:
12 ten rupee notes.

Test Case 2:
5 hundred rupee notes.

Test Case 3:
1 two rupee note, 1 five rupee note and 2 one rupee note.

'''

#code

def min_notes(n):
    notes = [1, 2, 5, 10, 50, 100]
    count = 0
    for i in range(5, -1, -1):
        while n >= notes[i]:
            n -= notes[i]
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(min_notes(n))