# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        output = []

        def helper(old_node):

            if not old_node:
                return
            output.append(TreeNode(old_node.val))
            helper(old_node.left)
            helper(old_node.right)

        helper(root)
        for i in output[1:]:
            root.left = None
            root.right = i
            root = i
