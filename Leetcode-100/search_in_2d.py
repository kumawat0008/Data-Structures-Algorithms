class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        my_row = -1

        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                my_row = i
            else:
                break

        return True if target in matrix[my_row][::] else False
