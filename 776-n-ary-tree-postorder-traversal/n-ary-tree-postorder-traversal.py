"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def tree(node):
            if not node:
                return

            for x in node.children:
                tree(x)
                res.append(x.val)
        tree(root)
        if root:
            res.append(root.val)
        return res