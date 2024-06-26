"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited={}

        def dfs(original):
            if original in visited:
                return visited[original]
            
            clone=Node(original.val)
            visited[original]=clone

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        return dfs(node)
