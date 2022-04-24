class Solution(object):
    def search_util(self, l, h, target, nums):
        if l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return self.search_util(l, mid - 1, target, nums)
            return self.search_util(mid + 1, h, target, nums)
        return h + 1

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_util(0, len(nums) - 1, target, nums)
