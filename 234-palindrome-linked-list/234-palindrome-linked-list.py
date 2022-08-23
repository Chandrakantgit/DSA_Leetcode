# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        s = ""
        while temp:
            s=s+str(temp.val)
            temp = temp.next
        print(s)
        i = 0
        j = len(s)-1-i
        while i<j:
            print(s[i],s[j])
            if s[i] != s[j]:
                return False
            print("here")
            i+=1
            j-=1
        return True
        