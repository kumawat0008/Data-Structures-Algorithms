# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_symmetric_util(a, b):
            if a is None and b is None:
                return True
            if a is not None and b is not None:
                return a.val == b.val and is_symmetric_util(a.left, b.right) and is_symmetric_util(a.right, b.left)

        return is_symmetric_util(root, root)
