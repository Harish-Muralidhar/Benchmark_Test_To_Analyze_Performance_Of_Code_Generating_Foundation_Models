
## Solution

- We can find the solution of Ax = b by taking the dot product of x with A, where A is a square matrix and x, b are vectors. 
- So we have to find a vector x where x is the dot product of A and x and b
- This is a kind of linear algebra problem and we can solve it using numpy
- We will get a vector x, we will have to print it in the form of a matrix
- We can convert the vector to matrix using numpy.reshape() function
- But the problem with this approach is that the matrix may not be symmetric, and we need a symmetric matrix
- So we will have to check if it is a symmetric matrix, if not we will have to find a symmetric matrix which is close to it.
- We can find a symmetric matrix which is close to a given matrix by taking the mean of it's original matrix and transpose of the matrix
- So now we have a symmetric matrix, it is not always possible to find a symmetric matrix close to the given matrix
- The only way we can check whether it is possible to find a symmetric matrix close to the given matrix is by checking the rank of the matrix.
- If the rank of the matrix is the same as the rank of the symmetric matrix, then we can find a symmetric matrix close to the given matrix.
- If the rank of the matrix is not the same as rank of the symmetric matrix, then we can find a symmetric matrix close to the given matrix
- If we are able to find a symmetric matrix close to the given matrix, then we can find a solution of Ax = b, else we can print -1



In[36]:


import numpy as np
import scipy
import scipy.linalg
def print_matrix(x):
    n = int(np.sqrt(x.shape[0]))
    x = np.array(x).reshape((n,n))
    for i in range(n):
        print(*x[i])
def find_matrix(A):
    b = [0 for i in range(A.shape[0])]
    b[-1] = 1
    b = np.array(b)
    x = scipy.linalg.solve(A, b)
    original_matrix = np.array(x).reshape((A.shape[0],1))
    symmetric_matrix = (original_matrix + original_matrix.T)/2
    if(np.linalg.matrix_rank(A) == np.linalg.matrix_rank(symmetric_matrix)):
        return symmetric_matrix.reshape((A.shape[0],))
    return -1
t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A = np.array(A)
    A = A.reshape((n,n))
    b = [0 for i in range(A.shape[0])]
    b[-1] = 1
    b = np.array(b)
    x = scipy.linalg.solve(A, b)
    original_matrix = np.array(x).reshape((A.shape[0],1))
    symmetric_matrix = (original_matrix + original_matrix.T)/2
    if(np.linalg.matrix_rank(A) == np.linalg.matrix_rank(symmetric_matrix)):
        print_matrix(symmetric_matrix.reshape((A.shape[0],)))
    else:
        print(-1)