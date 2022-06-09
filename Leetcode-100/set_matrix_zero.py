class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rows_zero = [-1] * rows
        cols_zero = [-1] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_zero[i] = 0
                    cols_zero[j] = 0

        for i in range(rows):
            for j in range(cols):
                if rows_zero[i] == 0 or cols_zero[j] == 0:
                    matrix[i][j] = 0

        return matrix
