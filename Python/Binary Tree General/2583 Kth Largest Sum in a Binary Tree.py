# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        root.level=0
        tbl=defaultdict(int)
        q=[root]
        while q:
            node=q.pop()
            tbl[node.level]+=node.val
            if node.left:
                node.left.level=node.level + 1
                q.append(node.left)
            if node.right:
                node.right.level=node.level+1
                q.append(node.right)
        lv=[tbl[k] for k in tbl]
        if k>len(lv): return -1
        lv.sort()
        return lv[-k]
