class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        def minPaths_util(row, col, m, n, dp, grid):

            if row > m or col > n:
                return float('inf')

            if row == m and col == n:
                return grid[row][col]

            if dp[row][col] != 0:
                return dp[row][col]

            down = grid[row][col] + minPaths_util(row + 1, col, m, n, dp, grid)

            right = grid[row][col] + minPaths_util(row, col + 1, m, n, dp, grid)
            dp[row][col] = min(right, down)
            return dp[row][col]

        return minPaths_util(0, 0, m - 1, n - 1, dp, grid)
