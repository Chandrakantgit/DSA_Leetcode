# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        st1 = []
        st2 = []
        ans =[]
        head = root
        st1.append(head)
        while st1 != []:
            temp = st1.pop()
            st2.append(temp)
            if temp.left:
                st1.append(temp.left)
            if temp.right:
                st1.append(temp.right)

        a = len(st2)
        for x in range(a):
            ans.append(st2.pop().val)
        return ans
            
        
        