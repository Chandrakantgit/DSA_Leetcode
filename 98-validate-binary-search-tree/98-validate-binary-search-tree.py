# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.inorder = []
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.inOrder(root)
        
        for x in range(0,len(self.inorder)-1):
            if self.inorder[x] >= self.inorder[x+1]:
                return False
        return True
            
            
    def inOrder(self,node):
        if node :
            self.inOrder(node.left)
            self.inorder.append(node.val)
            self.inOrder(node.right)
        