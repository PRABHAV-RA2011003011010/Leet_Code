# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=[]
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        def min_diff(arr):
            minimum=float('inf')
            for i in range(1,len(arr)):
                minimum=min(minimum,arr[i]-arr[i-1])
            return minimum
        inorder(root)
        return min_diff(res)
        