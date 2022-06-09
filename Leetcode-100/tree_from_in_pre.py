# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def build_tree_util(inorder):
            if not inorder:
                return None
            root = preorder.pop(0)
            tnode = TreeNode(root)
            in_index = inorder.index(root)
            tnode.left = build_tree_util(inorder[:in_index])
            tnode.right = build_tree_util(inorder[in_index + 1:])
            return tnode

        return build_tree_util(inorder)