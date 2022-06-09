class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = [-1] * len(height)
        right_max = [-1] * len(height)
        left_max[0] = height[0]

        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        res = 0
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]
        return res

