class Solution(object):

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def permute_util(self, nums, ptr, n, res):
        if ptr == n:
            res.append(list(nums))
        else:
            for i in range(ptr, n + 1, 1):
                self.swap(nums, ptr, i)
                self.permute_util(nums, ptr + 1, n, res)
                self.swap(nums, ptr, i)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permute_util(nums, 0, len(nums) - 1, res)
        return res
