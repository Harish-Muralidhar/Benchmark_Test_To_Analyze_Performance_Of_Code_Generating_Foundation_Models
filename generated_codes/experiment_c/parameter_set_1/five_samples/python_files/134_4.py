"""

(1, 4, 2, 3) -> (4, 2) -> (4)


(2, 3, 4, 1) -> (3, 4) -> (4)
	

(4, 3, 2, 1) -> (4, 2) -> (4)


(2, 1, 4, 3) -> (2, 3) -> (3)


(3, 4, 1, 2) -> (3, 1) -> (3)


(1, 4, 3, 2) -> (4, 3) -> (4)
	

(3, 2, 1, 4) -> (3, 1) -> (3)


(1, 3, 4, 2) -> (3, 4) -> (4)


(4, 2, 1, 3) -> (4, 2) -> (4)


(2, 4, 3, 1) -> (2, 3) -> (3)
	

(3, 1, 2, 4) -> (3, 2) -> (3)


(2, 1, 3, 4) -> (2, 3) -> (3)


(3, 4, 2, 1) -> (3, 4) -> (4)


(4, 3, 1, 2) -> (4, 3) -> (4)
"""

# Write your code below.
K = int(input())
n = 2**K 
dp = [0]*n
for i in range(n):
    for j in range(n):
        if (j >> i) & 1:
            dp[j] += 1 
for i in range(1,n):
    print(dp[i]%(10**9 + 9))