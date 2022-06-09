# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorderTraversalUtil(root, res):
            if root is not None:
                inorderTraversalUtil(root.left, res)
                res.append(root.val)
                inorderTraversalUtil(root.right, res)

        res = []
        inorderTraversalUtil(root, res)
        return res
