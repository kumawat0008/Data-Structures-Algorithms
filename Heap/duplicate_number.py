class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = set()
        for num in nums:
            if num in m:
                return num
            else:
                m.add(num)

