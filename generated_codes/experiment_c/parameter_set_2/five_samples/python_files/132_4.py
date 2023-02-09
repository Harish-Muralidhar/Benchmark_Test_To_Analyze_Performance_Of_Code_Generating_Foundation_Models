'''

Explanation

Harry grabs 6 books. He grabs the books in the following order:

english, mathematics, geography, graphics, english, mathematics

He wants to do a book exercise. He looks at the pile and finds that mathematics has the minimum number of remaining exercises. He removes the books above mathematics and picks mathematics. He does all the remaining exercises and trashes the book.

He grabs another book. He grabs graphics.

He wants to do a book exercise. He looks at the pile and finds that graphics has the minimum number of remaining exercises. He removes the books above graphics and picks graphics. He does all the remaining exercises and trashes the book.

'''

import heapq

class Book:
    def __init__(self, name, remaining):
        self.name = name
        self.remaining = remaining
    
    def __lt__(self, other):
        return self.remaining < other.remaining
    
    def __eq__(self, other):
        return self.remaining == other.remaining and self.name == other.name
    
    def __str__(self):
        return self.name + " " + str(self.remaining)

class BookStack:
    def __init__(self):
        self.stack = []
    
    def push(self, book):
        heapq.heappush(self.stack, book)
    
    def pop(self):
        return heapq.heappop(self.stack)
    
    def remove(self, book):
        self.stack.remove(book)
        heapq.heapify(self.stack)
    
    def peek(self):
        return self.stack[0]
    
    def __str__(self):
        return str([str(book) for book in self.stack])

def main():
    n = int(input())
    book_stack = BookStack()
    for i in range(n):
        line = input()
        if line.startswith("-"):
            if len(book_stack.stack) == 0:
                continue
            book = book_stack.peek()
            print