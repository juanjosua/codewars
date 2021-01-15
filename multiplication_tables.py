"""
Multiplication Tables
LINK: https://www.codewars.com/kata/5432fd1c913a65b28f000342/train/python

Description:

Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized according to the given dimensions. **The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.

Example:

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in its first column.

"""

def multiplication_table(row,col):
    # Good Luck!
    arr = [[i*j for i in range(1, col+1)] for j in range(1, row+1)]
    print(arr)

# best practices code
def multiplication_table(row,col):
    return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]

# # test code
multiplication_table(3,3)