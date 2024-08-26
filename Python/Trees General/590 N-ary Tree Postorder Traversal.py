"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res=[]

        #dfs
        def dfs(root):
            for child in root.children:
                dfs(child)
            res.append(root.val)
        
        dfs(root)

        return res
