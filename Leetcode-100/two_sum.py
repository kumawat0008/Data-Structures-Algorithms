class Solution:
    def twoSum(self, nums, target):
        res_list = [-1, -1]
        ind_map = dict()
        for index, num in enumerate(nums):
            res_list[0] = index
            if target-num in ind_map:
                res_list[1]=ind_map[target-num]
                break
            else:
                ind_map[num]=index
        return res_list