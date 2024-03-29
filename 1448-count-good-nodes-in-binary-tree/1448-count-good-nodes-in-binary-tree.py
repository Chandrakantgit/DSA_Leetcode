# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return self.count
        maxi = root.val
        
        def traverse(root,maxi):
            if root is None:
                return
            else:
                if root.val >= maxi:
                    maxi = root.val
                    self.count+=1
                traverse(root.left,maxi)
                traverse(root.right,maxi)
                
        traverse(root,maxi)
        return self.count
        