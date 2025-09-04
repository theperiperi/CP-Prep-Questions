"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        head = root
        while head:
            dummy = Node(0)
            temp = dummy

            while head:
                if head.left:
                    dummy.next = head.left
                    dummy = dummy.next
                if head.right:
                    dummy.next = head.right
                    dummy = dummy.next
                head = head.next
            head = temp.next
        return root
