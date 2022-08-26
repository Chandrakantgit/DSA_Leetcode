# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     Recursive Code 

    # ans = []
    # def __init__(self):
    #     self.ans =[]
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root:
    #         self.inorderTraversal(root.left)
    #         self.ans.append(root.val)
    #         self.inorderTraversal(root.right)
    #     return self.ans
    
# Iterative code
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if stack == []:
                    break
                else:
                    node = stack.pop()
                    ans.append(node.val)
                    node = node.right
        return ans
                
        
        