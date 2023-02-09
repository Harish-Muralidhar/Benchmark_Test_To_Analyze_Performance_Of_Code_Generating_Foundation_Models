'''

Explanation
Harry grabs the books one-by-one in the order: english, mathematics, geography, graphics.
The pile of books is:

english (9 remaining exercises)
mathematics (6 remaining exercises)
geography (8 remaining exercises)
graphics (3 remaining exercises)

When he wants to do a book exercise, the pile of books is:

mathematics (6 remaining exercises)
geography (8 remaining exercises)
graphics (3 remaining exercises)

The book with the minimum number of remaining exercises is mathematics. He removes the books above it and returns them to the messy floor.

The pile of books is:

graphics (3 remaining exercises)

When he wants to do a book exercise, the pile of books is:

graphics (3 remaining exercises)

The book with the minimum number of remaining exercises is graphics. He removes the books above it and returns them to the messy floor.

The pile of books is empty.

'''

import sys

class Book:
    def __init__(self, name, remaining):
        self.name = name
        self.remaining = remaining

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
    
    def push(self, item):
        if len(self.stacks) == 0 or self.stacks[-1].size() == self.capacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(item)
    
    def pop(self):
        if len(self.stacks) == 0:
            return None
       