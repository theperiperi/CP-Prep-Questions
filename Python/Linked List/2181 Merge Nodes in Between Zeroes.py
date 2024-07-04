# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        ptr=head.next
        sum=0
        while ptr.val!=0:
            sum+=ptr.val
            ptr=ptr.next
        
        head.next.val=sum
        head.next.next=self.mergeNodes(ptr)
        return head.next
