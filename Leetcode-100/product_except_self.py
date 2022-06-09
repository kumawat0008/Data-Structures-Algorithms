class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        flag = 0
        for i in nums:
            if i == 0:
                flag += 1
            else:
                product *= i
        res = [0] * len(nums)
        for i in range(len(nums)):
            if flag > 1:
                res[i] = 0
            elif flag == 1 and nums[i] != 0:
                res[i] = 0
            elif flag == 1 and nums[i] == 0:
                res[i] = product
            else:
                res[i] = product // nums[i]
        return res
