'''


'''

import numpy as np

#Read n
n = int(input())

#Create nxn matrix to store all the time values
time_values = np.zeros((n,n))

#Read input 
for i in range(n):
    time_values[i] = [int(x) for x in input().split()]
print(time_values)

#Find the indices of the minimum value in each column
minimum = np.argmin(time_values, axis=0)
print(minimum)

#Sort the minimum indices
sorted_minimum = np.sort(minimum)
print(sorted_minimum)

#Find the indices of the maximum value in each row
maximum = np.argmax(time_values, axis=1)
print(maximum)

#Check whether each element of sorted_minimum is present in maximum 
#If not present print -1
for i in sorted_minimum:
    if i not in maximum:
        print(-1)
        break
    else:
        continue

#If present print sorted_minimum
print(sorted_minimum+1)