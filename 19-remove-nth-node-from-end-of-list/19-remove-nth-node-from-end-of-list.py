# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        for i in range(n):
            p1 = p1.next
            p2 = head
        while p1:
            p2 = p2.next
            p1 = p1.next
        return p2  
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        delete = self.findFromEnd(dummy, n+1)
        delete.next = delete.next.next
        return dummy.next
        
