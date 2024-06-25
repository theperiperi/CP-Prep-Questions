# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.combined_sum=0

        def reverse_inorder_traversal(node):
            if not node:
                return 
            reverse_inorder_traversal(node.right)
            self.combined_sum+=node.val
            node.val=self.combined_sum

            reverse_inorder_traversal(node.left)
        reverse_inorder_traversal(root)
        return root
