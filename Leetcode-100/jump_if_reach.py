class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        target = nums[n - 1]
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= target:
                target = i
        return target == 0
