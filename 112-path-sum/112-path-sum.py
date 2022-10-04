# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(node):
            if node.left is None and node.right is None:
                return True
            else:
                return False
        
        
        def checkPathSum(node,requiredSum):
            
            if node is None:
                return False
                
            
            if node.val == requiredSum and isLeaf(node):
                return True
            
            left = checkPathSum(node.left,requiredSum-node.val)
            right = checkPathSum(node.right,requiredSum - node.val)
            return left or right
        return checkPathSum(root,targetSum)
                
            
            
        