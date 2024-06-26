# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        
        
        def build_bst(values):
            if not values: 
                return None
            mid=len(values)//2
            root=TreeNode(values[mid])
            root.left=build_bst(values[:mid])
            root.right=build_bst(values[mid+1:])
            return root
        return build_bst(inorder(root))
