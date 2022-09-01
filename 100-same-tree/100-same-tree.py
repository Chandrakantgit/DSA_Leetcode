# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSameTree(aTree,bTree):
            if aTree and bTree:
                if aTree.val == bTree.val:
                    
                    a = isSameTree(aTree.left,bTree.left)
                    b = isSameTree(aTree.right,bTree.right)
                    return a and b
                else:
                    return False
            
            elif aTree and not bTree:
                return False
            
            elif not aTree and bTree:
                return False
            elif not aTree and not bTree:
                return True
        
        return isSameTree(p,q)
            
    
  