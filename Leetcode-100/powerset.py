class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(index, n, temp, res, nums):
            if index == n:
                res.append(list(temp))
                return
            temp.append(nums[index])
            helper(index + 1, n, temp, res, nums)
            temp.pop()
            helper(index + 1, n, temp, res, nums)

        res = []
        n = len(nums)
        temp = []
        helper(0, n, temp, res, nums)
        return res

