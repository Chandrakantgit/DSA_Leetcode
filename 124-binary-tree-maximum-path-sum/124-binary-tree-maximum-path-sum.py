# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxPath(node,maxValue):
            if node is  None: return 0
            left = max(0,maxPath(node.left,maxValue))
            right = max(0,maxPath(node.right,maxValue))
            maxValue[0] = max(maxValue[0],left+right+node.val)
            return max(left,right)+node.val
        
        if root is None:
            return 0
        maxValue = [-100000]
        maxPath(root,maxValue)
        return maxValue[0]
        
        
        
        