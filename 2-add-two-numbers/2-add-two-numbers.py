# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = ""
        mun = ""
        temp = l1
        while temp:
            num = str(temp.val) + num
            temp = temp.next
        temp = l2
        while temp:
            mun =str(temp.val) + mun
            temp = temp.next
        sum = str(int(num)+int(mun))[::-1]
        i = 0
        resultList = ListNode(str(sum)[i])
        temp = resultList
        i = i + 1
        try:
            while(i):
                tempo = ListNode(str(sum)[i])
                temp.next = tempo
                temp = temp.next
                i+=1
        except:
            return resultList
                
                
            
        