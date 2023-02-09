'''

Explanation

Harry's pile initially is empty. He grabs the book with the name "english" and the number of remaining exercises is 9. So, he puts this book on top of the pile. Then, he grabs the book with the name "mathematics" and the number of remaining exercises is 6. Therefore, he puts this book on top of the pile. Finally, he grabs the book with the name "geography" and the number of remaining exercises is 8. So, he puts this book on top of the pile.
Now, he wants to do a book exercise. So, he needs to pick the book with the minimum number of remaining exercises. The books with the minimum number of remaining exercises are "mathematics" and "geography". Since he needs to remove the least number of books to pick the book, he picks "mathematics". So, he removes all the books above it, which is one book "geography". Then, he does all the remaining exercises of this book and throws it away.
Then, he grabs the book with the name "graphics" and the number of remaining exercises is 3. So, he puts this book on top of the pile. Finally, he wants to do a book exercise. He picks the book with the minimum number of remaining exercises, which is "graphics". Since there are no books above it, he removes zero books. Then, he does all the remaining exercises of this book and throws it away.
'''

import heapq
import bisect

n = int(input())
pile = []
heap = []

for _ in range(n):
  inp = input().split()
  if inp[0] == '-1':
    book = heapq.heappop(pile)
    print(bisect.bisect_left(pile, book), book[1])
  else:
    heapq.heappush(pile, (int(inp[0]), inp[1]))