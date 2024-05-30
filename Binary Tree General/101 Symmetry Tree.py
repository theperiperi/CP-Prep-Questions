# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return 1
            if not p or not q:
                return 0
            if p.val==q.val and same(p.left,q.right) and same(p.right,q.left):
                return 1
            return 0
        return same(root.left,root.right)
