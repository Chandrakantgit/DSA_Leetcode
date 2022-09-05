"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        
        def solve(k):
            if k:
                newk , ans = [],[]
                for x in k:
                    ans.append(x.val)
                    print(x.val)
                    if x.children is not None:
                        for y in x.children:
                            newk.append(y)
                res.append(ans)
                solve(newk)
                return
            else:
                return 
#             if len(k)==0:
#                 return
            
#             ans , newk= [], []
#             for node in k:
#                 ans.append( node.val )
                
#                 if node.left:
#                     newk.append(node.left)
#                 if node.right:
#                     newk.append(node.right)
            
            res.append(ans)
            solve( newk )
            return
        
        res = []
        if root:
            res.append([root.val])
            solve( root.children )
        return res
            
        
        