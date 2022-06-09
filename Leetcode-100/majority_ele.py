class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        n = len(nums)
        for num in nums:
            try:
                m[num] += 1
            except:
                m[num] = 1
            if m[num] > n // 2:
                return num
