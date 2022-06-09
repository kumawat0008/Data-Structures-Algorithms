class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(n, dp):
            if n == 0 or n == 1:
                return 1
            if dp[n]:
                return dp[n]
            count = 0
            for i in range(1, n + 1):
                count += helper(i - 1, dp) * helper(n - i, dp)
            dp[n] = count
            return count

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        return helper(n, dp)


