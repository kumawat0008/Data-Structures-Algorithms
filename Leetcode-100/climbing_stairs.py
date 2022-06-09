class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [0] * n

        def climb_util(step, n):

            if step == n:
                return 1
            if step > n:
                return 0
            if DP[step]:
                return DP[step]
            DP[step] = climb_util(step + 1, n) + climb_util(step + 2, n)
            return DP[step]

        return climb_util(0, n)
