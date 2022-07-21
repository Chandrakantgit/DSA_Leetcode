# Definition for singly-linked list. 
# class ListNode: 
#     def __init__(self, val=0, next=None): 
#         self.val = val 
#         self.next = next 
class Solution: 
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        temp = head 
        i=0 
        while i<left-1: 
            temp = temp.next 
            i+=1 
        temp2 = temp 
        j=i 
        while j < right-1: 
            temp2= temp2.next 
            j+=1 
        arr=[] 
        temp3 = temp 
        while temp3 != temp2.next: 
            arr.append(temp3.val) 
            temp3=temp3.next 
             
        while temp != temp2.next: 
            temp.val = arr.pop() 
            temp=temp.next 
        return head