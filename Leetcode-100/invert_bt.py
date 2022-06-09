# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def invert_util(root):
            if root is None:
                return

            invert_util(root.left)
            invert_util(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root

        invert_util(root)
        return root
