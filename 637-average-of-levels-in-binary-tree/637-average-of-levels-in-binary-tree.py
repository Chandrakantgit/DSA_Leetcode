# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def solve(k):
            if len(k)==0:
                return
            
            ans , newk= [], []
            for node in k:
                ans.append( node.val )
                
                if node.left:
                    newk.append(node.left)
                if node.right:
                    newk.append(node.right)
            
            res.append(ans)
            solve( newk )
            return
        
        res = []
        if root:
            solve( [root] )
        ans = []
        for x in res:
            sumi = 0
            count = 0
            for e in x:
                sumi+=e
                count+=1
            ans.append(sumi/count)
        return ans
        