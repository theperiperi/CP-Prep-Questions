# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeStore = {}
        children = set()

        for parent, child, isLeft in descriptions:
            children.add(child)
            node = TreeNode(child) if child not in nodeStore else nodeStore[child]

            if parent not in nodeStore:
                nodeStore[parent] = TreeNode(parent)

            if isLeft:
                nodeStore[child] = nodeStore[parent].left = node
            else:
                nodeStore[child] = nodeStore[parent].right = node

        for node in nodeStore.keys():
            if node not in children:
                return nodeStore[node]
