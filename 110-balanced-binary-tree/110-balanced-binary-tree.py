# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1
        
    def checkHeight(self,root):
        if root is None :
            return 0 
        
        lheight = self.checkHeight(root.left)
        if lheight == -1: return -1
        rheight = self.checkHeight(root.right)
        if rheight == -1: return -1
        
        if abs(lheight-rheight) > 1:return -1
        return max(lheight,rheight)+1
        
        
        