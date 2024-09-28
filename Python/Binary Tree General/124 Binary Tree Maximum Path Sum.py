# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')

        def calculateMaxGain(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left_gain = max(0, calculateMaxGain(node.left))
            right_gain = max(0, calculateMaxGain(node.right))

            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)

        calculateMaxGain(root)
        return max_sum
