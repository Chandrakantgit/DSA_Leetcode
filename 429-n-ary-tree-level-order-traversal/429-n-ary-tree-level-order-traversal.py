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
                    if x.children:
                        for y in x.children:
                            newk.append(y)
                res.append(ans)
                solve(newk)
                return
            else:
                return 
        
        res = []
        if root:
            res.append([root.val])
            solve( root.children )
        return res
            
        
        