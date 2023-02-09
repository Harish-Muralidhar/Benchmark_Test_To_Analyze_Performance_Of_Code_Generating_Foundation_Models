'''


'''

#Solution:

# Python 3 program to find the min  
# button presses to get the target 
# grid from initial grid 
  
# To find the number of button  
# presses required to get the 
# target matrix 
def findMinPresses(target, initial, n): 
    count = 0
    # To check whether the target  
    # grid can be achieved or not 
    for i in range(n): 
        for j in range(n): 
            if target[i][j] != initial[i][j]: 
                count += 1
    if count % 2 != 0: 
        return -1
    else: 
        return count // 2
  
# To find the row and column  
# indices to be pressed 
def findRowCol(target, initial, n): 
    row = [0 for i in range(n)] 
    col = [0 for i in range(n)] 
    for i in range(n): 
        for j in range(n): 
            if target[i][j] != initial[i][j]: 
                row[i] = 1
                col[j] = 1
    return row, col
  
# Driver code 
if __name__ == "__main__": 
    t = int(input())
    for i in range(t):
        n = int(input())
        initial = []
        final = []
        for i in range(n):
            initial.append(list(map(int,input().split())))
        for i in range(n):
            final.append(list(map(int,input().split())))
        row, col = findRowCol(final, initial, n) 
        count = findMinPresses(final, initial, n) 
        for i in range(n): 
            if row[i] == 1: 
                print(i, end = " ") 
        print() 
        for i in range(n): 
            if col[i] == 1: 
                print(i, end = " ") 
        print() 
        print(count)
'''
Another Method:

def gridChange(initial, final):
    # if the initial and final grids are the same, return 0
    if initial == final:
        return 0
    # if not, create a copy of the initial grid
    initialCopy = initial.copy()
    # create a list to store the total number of presses
    # and the rows and columns to be pressed
    pressCount = []
    # check if the final and initial grids are different
    if initial != final:
        # if they are, go through each row in the initial grid
        for row in range(len(initial)):
            # for each row, go through each column in the initial grid
            for col in range(len(initial[row])):
                # if the value in the initial grid is not equal to the final grid,
                # toggle the value in the initial grid copy
                if initial[row][col] != final[row][col]:
                    initialCopy[row][col] = toggle(initialCopy[row][col])
                # if the initial grid copy is equal to the final grid after toggling,
                # add the row and column to the pressCount list
                if initialCopy == final:
                    pressCount.append([row, col])
        # add the number of presses to the pressCount list
        pressCount.append(len(pressCount))
        # return the pressCount list
        return pressCount

# create a function to toggle 1s to 0s and 0s to 1s
def toggle(num):
    # if the number is a 1, return a 0
    if num == 1:
        return 0
    # if the number is a 0, return a 1
    elif num == 0:
        return 1

# get the number of grids to check
numGrids = int(input())
# for each grid to check,
for grid in range(numGrids):
    # get the size of the grid
    size = int(input())
    # create an empty initial grid
    initial = []
    # for each row in the grid,
    for row in range(size):
        # get the initial values in that row
        rowValues = [int(x) for x in input().split()]
        # add the values to the initial grid
        initial.append(rowValues)
    # create an empty final grid
    final = []
    # for each row in the grid,
    for row in range(size):
        # get the final values in that row
        rowValues = [int(x) for x in input().split()]
        # add the values to the final grid
        final.append(rowValues)
    # check the minimum number of presses and the rows and columns to be pressed
    pressCount = gridChange(initial, final)
    # if the pressCount is not 0,
    if pressCount != 0:
        # check the number of presses
        numPresses = pressCount[-1]
        # print the number of presses
        print(numPresses)
        # create a string to store the row indices
        rowIndices = ""
        # create a string to store the column indices
        colIndices = ""
        # for each row and column in the pressCount,
        for row, col in pressCount[:-1]:
            # add the row and column indices to the rowIndices and colIndices strings
            rowIndices += str(row) + " "
            colIndices += str(col) + " "
        # print the rowIndices and colIndices strings
        print(rowIndices)
        print(colIndices)
    # if the pressCount is 0, print 0
    else:
        print("0")
'''