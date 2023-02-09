"""


"""

import numpy as np

n = int(input("Enter the size of the map: "))
k = int(input("Enter the size of the trap: "))

# Create a numpy array of size nxn
A = np.zeros((n,n))

# Input the values of the array
for i in range(n):
    for j in range(n):
        A[i][j] = int(input())

# Create a numpy array of size (n-k+1)x(n-k+1)
B = np.zeros((n-k+1,n-k+1))

# Find the sum of the elements in each subarray of size kxk
for i in range(n-k+1):
    for j in range(n-k+1):
        B[i][j] = np.sum(A[i:i+k,j:j+k])

# Find the minimum value in each row of B
C = np.zeros((n-k+1,1))
for i in range(n-k+1):
    C[i] = np.min(B[i,:])

# Find the index of the minimum value in each row of B
D = np.zeros((n-k+1,1))
for i in range(n-k+1):
    D[i] = np.argmin(B[i,:])

# Print the final output
for i in range(n-k+1):
    for j in range(n-k+1):
        if j == D[i]:
            print(C[i],end=" ")
        else:
            print(0,end=" ")
    print()