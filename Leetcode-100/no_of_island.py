class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def mark_land(grid, x, y, m, n):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            mark_land(grid, x - 1, y, m, n)
            mark_land(grid, x + 1, y, m, n)
            mark_land(grid, x, y - 1, m, n)
            mark_land(grid, x, y + 1, m, n)

        m = len(grid)
        n = len(grid[0])
        island = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    mark_land(grid, x, y, m, n)
                    island += 1
        return island
