# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        flag = True # for left to right,flag will be false if it is from right to left
        stack = [root]
        ans = []
        while stack != []:
            if flag:
                temp = []
                tempAns = []
                while stack!=[]:
                    node = stack.pop()
                    tempAns.append(node.val)
                    print("appending",node.val)
                    if node.left : temp.append(node.left)
                    if node.right: temp.append(node.right)
                stack = stack + temp
                ans.append(tempAns)
                flag = not flag
            else:
                temp = []
                tempAns = []
                while stack!=[]:
                    node = stack.pop()
                    tempAns.append(node.val)
                    if node.right :temp.append(node.right)
                    if node.left :temp.append(node.left)
                    
                stack = stack + temp
                ans.append(tempAns)
                flag = not flag
        print(ans)
        return ans
                
                    
                
            
        