class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def uniquePaths_util(row, col, m, n, dp):

            if row == m and col == n:
                return 1
            if row > m or col > n:
                return 0
            if dp[row][col] != 0:
                return dp[row][col]
            dp[row][col] = uniquePaths_util(row + 1, col, m, n, dp) + uniquePaths_util(row, col + 1, m, n, dp)
            return dp[row][col]

        dp = [[0 for i in range(n)] for j in range(m)]
        return uniquePaths_util(0, 0, m - 1, n - 1, dp)

