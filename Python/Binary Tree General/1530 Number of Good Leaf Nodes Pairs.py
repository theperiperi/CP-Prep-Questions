# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0

        def solve(root):
            if root is None:
                return {}
            if root.left is None and root.right is None:
                # leaf node here
                return {1: 1}
            lhNodes = solve(root.left)            
            rhNodes = solve(root.right)
            
            for leftNodeHeight in lhNodes:
                for rightNodeHeight in rhNodes:
                    if leftNodeHeight + rightNodeHeight <= distance:
                        self.res += lhNodes[leftNodeHeight] * rhNodes[rightNodeHeight]

            nhNodes = {}
            for key in lhNodes:
                if key <= distance:
                    nhNodes[key + 1] = lhNodes[key]
            for key in rhNodes:
                if key <= distance:
                    nhNodes[key + 1] = nhNodes.get(key + 1, 0) + rhNodes[key]                    



            return nhNodes

        solve(root)
        return self.res
