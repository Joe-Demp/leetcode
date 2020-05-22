# A magic square is an n x n matrix of distinct positive integers from 1 to n^2 where
# the sum of any row, column or diagonal is always equal to the same number, the magic constant

# Given a 3 x 3 matrix s, convert s to a magic square, minimizing costs
# the cost of replacing digit a with digit b is |a - b|
# The resulting magic square must contain distinct integers in range [1, 9]

def diagonal_sums(matrix):
    sum1 = 0
    sum2 = 0
    for i in range(3):
        sum1 += matrix[i][i]
        sum2 += matrix[i][2 - i]
    return(sum1, sum2)

def row_sums(matrix):
    return ([sum(row) for row in matrix])

def col_sums(matrix):
    tuple([sum(row[i]) for row in matrix for i in range(3)])

def is_magic(matrix):
    sums = [*diagonal_sums(matrix), *row_sums(matrix), *col_sums(matrix)]
    return sums.count(sums[0]) == len(sums)

def formingMagicSquare(s):
    pass
