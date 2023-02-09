'''



Explanation
In the first case, employee 1 should get at least 10$ more than employee 2, employee 2 should get at least 20$ more than employee 3, employee 1 should get at least 40$ more than employee 3, and employee 2 should get at least 5$ more than employee 4. So, employee 1 should get at least 50$ more than employee 4. So, the minimum total bonus is 460$.

In the second case, employee 1 should get at least 10$ more than employee 2, employee 2 should get at least 10$ more than employee 3, and employee 3 should get at least 10$ more than employee 1. So, this is inconsistent, and it’s not possible to distribute bonus among them.

Note: 

The bonus of each employee should be a non-negative integer.

'''

# Write your code here
#import numpy as np
import numpy as np

def bonus(N,M,L,matrix):
    #print(matrix)
    #print(np.shape(matrix))
    #print(np.shape(matrix)[0])
    #print(np.shape(matrix)[1])
    #print(np.shape(matrix)[2])
    for i in range(np.shape(matrix)[0]):
        for j in range(np.shape(matrix)[1]):
            for k in range(np.shape(matrix)[2]):
                if matrix[i,j,k] == 1:
                    matrix[i,j,k] = L
                else:
                    matrix[i,j,k] = 0
    #print(matrix)
    #print(np.shape(matrix))
    #print(np.shape(matrix)[0])
    #print(np.shape(matrix)[1])
    #print(np.shape(matrix)[2])
    #print(np.sum(matrix,axis=2))
    #print(np.sum(matrix,axis=1))
    #print(np.sum(matrix,axis=0))
    #print(np.sum(np.sum(matrix,axis=2),axis=