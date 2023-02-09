'''

Explanation

Test Case 1:
12 ten rupee notes

Test Case 2:
5 hundred rupee notes

Test Case 3:
1 two hundred rupee note + 1 twenty rupee note + 1 two rupee note
'''

#Solution

def count(n):
    count = 0
    notes = [100, 50, 10, 5, 2, 1]
    for i in notes:
        count += n//i
        n = n%i
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(count(n))