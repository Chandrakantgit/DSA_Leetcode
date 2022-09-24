# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        Ans = []
        
        def isLeaf(node):
            if node.left is None and node.right is None:
                return True
            else:
                False
        
        def pathGive(node,requiredSum,ds):
            if node is None:
                return
            
            if isLeaf(node):
                ds.append(node.val)
                if requiredSum - node.val == 0:
                    a = list()
                    for x in ds:
                        a.append(x)
                    Ans.append(a)
                    return
                else:
                    return
            else:
                ds.append(node.val)
                if node.left and node.right:
                    
                    pathGive(node.left,requiredSum - node.val,ds)
                    ds.pop()
                    pathGive(node.right,requiredSum - node.val,ds)
                    ds.pop()
                elif node.left:
                    pathGive(node.left,requiredSum - node.val,ds)
                    ds.pop()
                else:
                    pathGive(node.right,requiredSum - node.val,ds)
                    ds.pop()
        
        pathGive(root,targetSum,[])
        return Ans
        