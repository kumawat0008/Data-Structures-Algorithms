class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res_list = list()
        length = len(nums)
        for i, num1 in enumerate(nums):
            if num1>0:
                break
            p = i+1
            q = length-1
            while p<q:
                if num1+nums[p]+nums[q]==0 and [num1, nums[p], nums[q]] not in res_list:
                    res_list.append([num1, nums[p], nums[q]])
                    p+=1
                elif num1+nums[p]+nums[q]<0:
                    p+=1
                else:
                    q-=1
        return res_list