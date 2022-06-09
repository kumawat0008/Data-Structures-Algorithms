# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def diameter(root):
            if root is None:
                return 0, 0
            ld, lh = diameter(root.left)
            rd, rh = diameter(root.right)
            h = max(lh, rh) + 1
            d = max(ld, rd, lh + rh + 1)
            return d, h

        d, h = diameter(root)
        return d - 1
