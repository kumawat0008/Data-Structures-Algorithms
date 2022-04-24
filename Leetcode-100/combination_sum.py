class Solution(object):
    def comb_util(self, candidates, target, ds, res, index):
        if target == 0:
            res.append(list(ds))
            return
        if target < 0:
            return
        if index >= len(candidates):
            return
        ds.append(candidates[index])
        self.comb_util(candidates, target - candidates[index], ds, res, index)
        ds.pop()
        self.comb_util(candidates, target, ds, res, index + 1)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        ds = []
        self.comb_util(candidates, target, ds, res, 0)
        return res
