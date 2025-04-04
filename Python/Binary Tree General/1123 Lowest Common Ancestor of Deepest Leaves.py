# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return depth, None
            left_depth, left_ancestor = dfs(node.left, depth + 1)
            right_depth, right_ancestor = dfs(node.right, depth + 1)

            if left_depth == right_depth :
                return left_depth, node
            elif left_depth > right_depth:
                return left_depth, left_ancestor
            else:
                return right_depth, right_ancestor
        return dfs(root, 0)[1]
