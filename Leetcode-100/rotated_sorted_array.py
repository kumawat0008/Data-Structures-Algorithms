class Solution(object):
    def search_util(self, l, h, target, nums):
        if l > h:
            return -1
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if target >= nums[l] and target <= nums[mid]:
                return self.search_util(l, mid - 1, target, nums)
            else:
                return self.search_util(mid + 1, h, target, nums)
        if target >= nums[mid] and target <= nums[h]:
            return self.search_util(mid + 1, h, target, nums)
        return self.search_util(l, mid - 1, target, nums)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_util(0, len(nums) - 1, target, nums)
