# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currentNode=dummyNode=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                currentNode.next=list1
                list1,currentNode=list1.next,list1   

            else:
                currentNode.next=list2
                list2,currentNode=list2.next,list2
                
            
        if list1 or list2:
            currentNode.next=list1 if list1 else list2
            
        return dummyNode.next
            
