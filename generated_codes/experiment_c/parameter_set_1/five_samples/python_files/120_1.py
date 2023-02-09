"""
Hence sum = 1+1+1+1+1+1 = 6.0
"""

"""
Solution:
Let us denote P(i, j) as the probability of reaching (i, j). For any cell (i, j), P(i, j) = P(i-1, j) + P(i, j-1).
This is because the probability of reaching (i, j) is the sum of the probability of reaching (i-1, j) and the probability of reaching (i, j-1).
This is a recursive formula.
Let us denote the required answer as S. Then S = P(1, 1) + P(2, 2) + P(3, 3) + ... + P(N, N).
This is because the probability of visiting a cell is the probability of reaching that cell.
So we see that S is the sum of the diagonal elements of the matrix P.
Now we can rewrite P(i, j) as P(i, j) = P(i-1, j) + P(i, j-1) = P(i-1, j) + P(i-1, j-1) + P(i-2, j-1) = ... = P(1, 1) + P(1, 2) + P(1, 3) + ... + P(1, j-1) + P(i-1, j-1)
This is because all the terms P(x, y) where x > i, y <= j have been cancelled by the previous terms of the recurrence.
So we see that P(i, j) = S(i, j) + S(i-1, j-1)
where S(i, j) = P(1, 1) + P(1, 2) + P(1, 3) + ... + P(1, j-1) + P(i-1, j-1)
So our final S = S(1, 1) + S(2, 2) + S(3, 3) + ... + S(N, N).
We can implement this recurrence in O(n^2) time.
"""