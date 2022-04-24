class Solution(object):
    def my_reverse(self, matrix, col, start, end):
        while start < end:
            matrix[start][col], matrix[end][col] = matrix[end][col], matrix[start][col]
            start += 1
            end -= 1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            self.my_reverse(matrix, i, 0, len(matrix) - 1)
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

