# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is [] or root is None:
            return []
        q = []
        level_so_far = 0
        level_map = dict()
        q.append((root, 0))
        while len(q):
            temp, level = q.pop(0)
            try:
                level_map[level].append(temp.val)
            except:
                level_map[level] = [temp.val]
            if temp.left is not None:
                q.append((temp.left, level + 1))
            if temp.right is not None:
                q.append((temp.right, level + 1))
            if level_so_far < level:
                level_so_far = level

        # print(level_map, level_so_far)
        res = []
        for i in range(level_so_far + 1):
            res.append(level_map[i])
        return res



