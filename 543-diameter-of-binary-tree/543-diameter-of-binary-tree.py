# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.heightFinder(root,ans)
        return ans[0]
        
        
    def heightFinder(self,root,ans):
        if root is None:
            return 0
        lheight = self.heightFinder(root.left,ans)
        rheight = self.heightFinder(root.right,ans)
        
        ans[0] = max(ans[0],lheight+rheight)
        
        return 1+max(lheight,rheight)
        