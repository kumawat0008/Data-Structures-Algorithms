# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def helper(root, count):
            if root is None:
                return None
            left = helper(root.left, count)
            if left is not None:
                return left
            count[0] -= 1
            if count[0] == 0:
                return root
            return helper(root.right, count)

        count = [k]
        return helper(root, count).val
