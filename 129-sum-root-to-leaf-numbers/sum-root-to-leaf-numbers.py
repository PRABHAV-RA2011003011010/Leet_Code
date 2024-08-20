# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        total=0
        s=str(root.val)
        def sumtree(root: Optional[TreeNode],s,total):
            if not root:
                return 0
            if not root.left and not root.right:
                s+=str(root.val)
                cur=int(s)
                total+=cur
                return total
            s+=str(root.val)
            return sumtree(root.left,s,total)+sumtree(root.right,s,total)
            
        
        return sumtree(root.left,s,total)+sumtree(root.right,s,total)
            
