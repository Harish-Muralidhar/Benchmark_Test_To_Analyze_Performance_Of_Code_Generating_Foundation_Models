'''

Explanation

Harry grabs the books one-by-one and adds the books that still have remaining exercises to the top of the pile.

The books are:

english (9 remaining exercises)
mathematics (6 remaining exercises)
geography (8 remaining exercises)

Harry wants to do a book exercise. He must remove 1 book to pick mathematics.

The books are:

english (9 remaining exercises)
geography (8 remaining exercises)

Harry grabs graphics (3 remaining exercises).

The books are:

english (9 remaining exercises)
geography (8 remaining exercises)
graphics (3 remaining exercises)

Harry wants to do a book exercise. He must remove 0 books to pick graphics.

The books are:

english (9 remaining exercises)
geography (8 remaining exercises)

'''

import heapq

class Book:
    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises
    def __lt__(self, other):
        if self.exercises == other.exercises:
            return self.name > other.name
        return self.exercises > other.exercises

def main():
    n = int(input())
    books = []
    for _ in range(n):
        line = input().split()
        if line[0] == '-1':
            book = heapq.heappop(books)
            print(len(books), book.name)
        else:
            heapq.heappush(books, Book(line[1], int(line[0])))

if __name__ == '__main__':
    main()