'''

'''

def get_period(x, P1, P2):
    '''
    Returns the period of x, P1 and P2
    '''
    if x == 0:
        period = P1
    elif x == 1:
        period = P2
    else:
        period = get_period(x - 2, P1, P2)
    return period

def get_values(row, column, matrix, P1, P2, period):
    '''
    Returns the values to be appended
    '''
    values = []
    if row == 0:
        values = [period]
    else:
        values.append(period)
        values.extend(matrix[row - 1][column])
    return values

def get_image_count(grid, P1, P2, move):
    '''
    Returns the total number of images in the grid, post the given move
    '''
    rows = len(grid)
    columns = len(grid[0])
    matrix = []
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(get_values(row, column, matrix, P1, P2, get_period(column, P1, P2)))
    for row in range(rows):
        for column in range(columns):
            if row == 0:
                grid[row][column] = max(1, grid[row][column])
            else:
                grid[row][column] = max(1, grid[row][column]) + len([x for x in matrix[row - 1][column] if x < move])
    return grid, matrix

def get_total_images(grid):
    '''
    Returns the total number of images in the grid
    '''
    return sum([sum(x) for x in grid])

def main():
    '''
    Driver function
    '''
    rows, columns, _ = map(int, input().split())
    row, column = map(int, input().split())
    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    grid[row - 1][column - 1] = 1
    p1 = [int(x) for x in input().split()]
    p2 = [int(x) for x in input().split()]
    for _ in range(int(input())):
        p1_index = 0
        p2_index = 0
        for _ in range(int(input())):
            grid, _ = get_image_count(grid, p1[p1_index], p2[p2_index], _ + 1)
            p1_index += 1
            p2_index += 1
            if p1_index == len(p1):
                p1_index = 0
            if p2_index == len(p2):
                p2_index = 0
        print(get_total_images(grid))
        grid = [[0 for _ in range(columns)] for _ in range(rows)]
        grid[row - 1][column - 1] = 1

if __name__ == '__main__':
    main()