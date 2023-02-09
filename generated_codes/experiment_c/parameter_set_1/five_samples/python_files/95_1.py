"""

Example 3

Input:
2 3
010
010

Output:
0

Explanation

In the first example, there are three sub rectangles which contain even number of currants.


In the second example, there are 26 such sub rectangles


In the third example, there is no such sub rectangle.

https://www.codechef.com/problems/CURRECT
"""

def number_of_rectangles_with_even_number_of_currants(cake_matrix):
    num_rows, num_cols = len(cake_matrix), len(cake_matrix[0])

    even_rect_count = 0
    odd_rect_count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            even_rect_count += i * j * cake_matrix[i][j]
            odd_rect_count += (i * (num_cols - j) + (num_rows - i) * j + (num_rows - i) * (num_cols - j)) * cake_matrix[i][j]

    return even_rect_count + odd_rect_count


if __name__ == '__main__':
    cake_matrix = [
        ['0', '1'],
        ['1', '0']
    ]
    print(number_of_rectangles_with_even_number_of_currants(cake_matrix))

    cake_matrix = [
        ['1', '0', '1', '0'],
        ['0', '1', '0', '1'],
        ['1', '1', '1', '0']
    ]
    print(number_of_rectangles_with_even_number_of_currants(cake_matrix))

    cake_matrix = [
        ['0', '1', '0'],
        ['0', '1', '0']
    ]
    print(number_of_rectangles_with_even_number_of_currants(cake_matrix))