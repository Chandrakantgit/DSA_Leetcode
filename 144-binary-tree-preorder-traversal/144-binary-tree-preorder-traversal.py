# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        if root == None:
            return preorder
        st = list()
        st.append(root)
        while st != []:
            root = st.pop()
            preorder.append(root.val)
            if root.right:
                st.append(root.right)
            if root.left:
                st.append(root.left)
        return preorder
        
        