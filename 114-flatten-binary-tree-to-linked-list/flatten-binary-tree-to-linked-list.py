# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root
        dict1={}
        cur=0
        def preorder(node):
            if not node:
                return 

            nonlocal cur
            dict1[cur]=node
            cur+=1
            preorder(node.left)
            preorder(node.right)

        
        preorder(root)

        cur_node=root
        next_node=1
        while next_node in dict1:
            cur_node.right=dict1[next_node]
            cur_node.left = None
            cur_node=cur_node.right
            next_node+=1
        cur_node.right= None
        return root
       






    
        