# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        res: dict[int, TreeNode] = {root.val: root}
        to_delete: set[int] = set(to_delete)

        def recursion(parent: TreeNode | None, cur_node: TreeNode | None, isleft: bool) -> None:
            nonlocal res
            if cur_node is None:
                return

            recursion(cur_node, cur_node.left, True)
            recursion(cur_node, cur_node.right, False)

            if cur_node.val in to_delete:
                if cur_node.val in res:
                    del res[cur_node.val]

                if parent:
                    if isleft:
                        parent.left = None
                    else:
                        parent.right = None

                if cur_node.left:
                    res[cur_node.left.val] = cur_node.left
                if cur_node.right:
                    res[cur_node.right.val] = cur_node.right

        recursion(None, root, False)
        return res.values()
        
