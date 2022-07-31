# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Applied DFS, goes deep inside the tree to find out p or q.
        #the moment we find p or q,it is returned. if both p and q are found hen the root at which they are found i returned.
        # IT IS A RECURSIVE SOLUTION.
        
        # Time complexity : O(n)
        # Auxiliary space complexity : O(n) (due tpo recursion stack)
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)        
        if left != None and right != None:
            return root
        elif left != None:
            return left
        elif right != None:
            return right
        