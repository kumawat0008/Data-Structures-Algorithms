class Solution(object):
    def jump_util(self, nums, index, dp):
        if index in dp:
            return dp[index]
        if index >= len(nums) - 1:
            return 0
        minJump = 9999999999999
        maxSteps = nums[index]
        while maxSteps > 0:
            minJump = min(minJump, 1 + self.jump_util(nums, index + maxSteps, dp))
            maxSteps = maxSteps - 1
        dp[index] = minJump
        return minJump

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = dict()
        return self.jump_util(nums, 0, dp)
