'''

Explanation

Test Case 1:
12 ten rupee notes

Test Case 2:
5 hundred rupee notes

Test Case 3:
1 two rupee note
1 ten rupee note
2 one rupee note

'''

#Solution

def currency_notes(n):
    notes = [100, 50, 10, 5, 2, 1]
    note_counter = [0, 0, 0, 0, 0, 0]
    print("Currency Count ->")
    for i, j in zip(notes, note_counter):
        if n // i != 0:
            j = n // i
            n = n - j * i
            print("{} : {}".format(i, j))

if __name__ == "__main__":
    n = int(input("Enter the amount: "))
    currency_notes(n)