#filter and reversal
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev,curr=None,head

        while curr:
            curr.next,prev,curr=prev,curr,curr.next
        
        curr,prev.next=prev.next,None

        while curr:
            temp=curr.next
            if curr.val>=prev.val:
                curr.next=prev
                prev=curr
            curr=temp
        return prev
