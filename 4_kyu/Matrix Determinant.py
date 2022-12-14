https://www.codewars.com/kata/52a382ee44408cea2500074c/python

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    mat = matrix[1:]
    res = 0
    sig = 1
    for i in range(n):
        minor = []
        for j in range(n-1):
            minor.append(mat[j][:i] + mat[j][i+1:])
        res += sig * matrix[0][i] * determinant(minor)
        sig *= -1
    return res