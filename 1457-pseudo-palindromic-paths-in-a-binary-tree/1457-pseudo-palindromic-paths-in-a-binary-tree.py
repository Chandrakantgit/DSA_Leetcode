# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
#it is a solution but too complex
#         ans = []
#         def PPP(node,string,ans):
#             if node is None:
#                 ans.append(int(string))
#                 return
#             string = string + str(node.val)
#             if node.left and node.right:
#                 PPP(node.left,string,ans)
#                 PPP(node.right,string,ans)
#             elif node.right is  None:
#                 PPP(node.left,string,ans)
#             elif node.left is None:
#                 PPP(node.right,string,ans)
#             else:
#                 return 
                
            
#         PPP(root,"",ans)
#         def checkpalindrome(num):
#             pairs = set()
#             for x in str(num):
#                 if x in pairs:
#                     pairs.remove(str(x))
#                 else:
#                     pairs.add(str(x))
            
#             if len(pairs) <= 1:
#                 return 1
#             else:
#                 return 0
#         answer =0
#         for x in ans:
#             answer += checkpalindrome(x)
      # return answer
    
        def traverse(node, pairs):
            if not node:
                return 0
            
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)
            
            if not node.left and not node.right:
                return 1 if len(pairs) <= 1 else 0
            
            left = traverse(node.left, set(pairs))
            right = traverse(node.right, set(pairs))
            
            
            return left + right
        
        return traverse(root, set())
        
            
            
            
        
        
        